import requests
import csv
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CSV_ARQUIVO = "repos_abap.csv"
ANO_INICIAL = 2008
ANO_FINAL = datetime.now().year
PER_PAGE = 100
SLEEP_ENTRE_CHAMADAS = 2.2

SEARCH_URL = "https://api.github.com/search/repositories"

session = requests.Session()
session.headers.update({
    "Accept": "application/vnd.github+json",
    "User-Agent": "abap-repo-scraper/1.0",
})
if GITHUB_TOKEN:
    session.headers.update({"Authorization": f"token {GITHUB_TOKEN}"})


def esperar_por_rate_limit(resp):
    retry_after = resp.headers.get("Retry-After")
    msg = ""
    try:
        msg = resp.json().get("message", "")
    except Exception:
        pass

    if retry_after:
        espera = max(int(retry_after), 1)
        print(f"403 (Retry-After). Aguardando {espera}s... Mensagem: {msg}")
        time.sleep(espera)
        return

    reset = resp.headers.get("X-RateLimit-Reset")
    if reset:
        agora = int(time.time())
        espera = max(int(reset) - agora, 5)
        espera = min(espera, 120)
        print(f"403 (Rate limit). Aguardando até o reset: {espera}s... Mensagem: {msg}")
        time.sleep(espera)
        return

    print(f"403 (Abuse detection). Aguardando 60s... Mensagem: {msg}")
    time.sleep(60)


def github_search(query: str, page: int):
    params = {
        "q": query,
        "sort": "size",
        "order": "desc",
        "per_page": PER_PAGE,
        "page": page
    }

    tentativas = 0
    while True:
        tentativas += 1
        try:
            resp = session.get(SEARCH_URL, params=params, timeout=20)
        except requests.exceptions.RequestException as e:
            espera = min(5 * tentativas, 30)
            print(f"Erro de rede: {e}. Tentando de novo em {espera}s...")
            time.sleep(espera)
            continue

        if resp.status_code == 403:
            esperar_por_rate_limit(resp)
            continue

        if resp.status_code in (502, 503, 504):
            espera = min(5 * tentativas, 30)
            print(f"Erro {resp.status_code} do servidor. Tentando em {espera}s...")
            time.sleep(espera)
            continue

        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            try:
                detalhe = resp.json()
            except Exception:
                detalhe = {}
            print(f"HTTP {resp.status_code} na busca. Detalhe: {detalhe}")
            raise e

        restante = resp.headers.get("X-RateLimit-Remaining")
        if restante is not None:
            print(f"Search API restante: {restante}")

        time.sleep(SLEEP_ENTRE_CHAMADAS)

        return resp.json()


def ultimo_dia_do_mes(ano: int, mes: int) -> int:
    if mes == 12:
        return 31
    return (datetime(ano, mes + 1, 1) - timedelta(days=1)).day


def processar_intervalo(data_inicio: str, data_fim: str, acumulador: list):
    page = 1
    while True:
        query = f"language:ABAP created:{data_inicio}..{data_fim}"
        data = github_search(query, page)

        total_count = int(data.get("total_count", 0))
        if page == 1 and total_count > 1000:
            inicio_dt = datetime.strptime(data_inicio, "%Y-%m-%d")
            fim_dt = datetime.strptime(data_fim, "%Y-%m-%d")
            meio_dt = inicio_dt + (fim_dt - inicio_dt) / 2

            parte1_ini = data_inicio
            parte1_fim = (meio_dt).strftime("%Y-%m-%d")
            parte2_ini = (meio_dt + timedelta(days=1)).strftime("%Y-%m-%d")
            parte2_fim = data_fim

            print(f"Intervalo {data_inicio}..{data_fim} tem {total_count} resultados. Subdividindo em:")
            print(f"   • {parte1_ini}..{parte1_fim}")
            print(f"   • {parte2_ini}..{parte2_fim}")

            processar_intervalo(parte1_ini, parte1_fim, acumulador)
            processar_intervalo(parte2_ini, parte2_fim, acumulador)
            return

        itens = data.get("items", [])
        if not itens:
            print(f"Intervalo {data_inicio}..{data_fim} finalizado (sem novos itens).")
            break

        print(f"Intervalo {data_inicio}..{data_fim} - Página {page} - {len(itens)} itens")

        for repo in itens:
            try:
                nome = repo.get("name", "")
                tamanho = repo.get("size", "")
                link = repo.get("html_url", "")
                criado = repo.get("created_at", "")
                acumulador.append([nome, tamanho, link, criado])
                print(f"   ➡️ {len(acumulador)}: {nome} ({tamanho} KB)")
            except Exception as e:
                print(f"Erro ao processar repositório: {e}")
                continue

        page += 1


def main():
    print("Iniciando busca de repositórios ABAP por ano/mês (ordenados por tamanho)...")
    todos = []

    for ano in range(ANO_INICIAL, ANO_FINAL + 1):
        for mes in range(1, 13):
            ld = ultimo_dia_do_mes(ano, mes)
            inicio = f"{ano}-{mes:02d}-01"
            fim = f"{ano}-{mes:02d}-{ld:02d}"

            try:
                processar_intervalo(inicio, fim, todos)
            except requests.exceptions.HTTPError as e:
                print(f"Erro no ano {ano}, mês {mes}: {e}")
                continue

    with open(CSV_ARQUIVO, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nome", "Tamanho (KB)", "Link", "Data de Criação"])
        writer.writerows(todos)

    print(f"\nArquivo {CSV_ARQUIVO} gerado com sucesso! ({len(todos)} repositórios salvos)")


if __name__ == "__main__":
    main()
