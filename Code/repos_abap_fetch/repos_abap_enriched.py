import pandas as pd
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

INPUT_FILE = "./Code/repos_abap_fetch/repos_abap_picked.csv"
OUTPUT_FILE = "./Code/repos_abap_fetch/repos_abap_enriched.csv"

session = requests.Session()
session.headers.update({
    "Accept": "application/vnd.github+json",
    "User-Agent": "abap-repo-enricher/1.0"
})
if GITHUB_TOKEN:
    session.headers.update({"Authorization": f"token {GITHUB_TOKEN}"})


def esperar_por_rate_limit(resp):
    reset = resp.headers.get("X-RateLimit-Reset")
    if reset:
        agora = int(time.time())
        espera = max(int(reset) - agora, 5)
        print(f"Rate limit atingido. Esperando {espera}s...")
        time.sleep(espera)
    else:
        print("Rate limit atingido. Esperando 60s...")
        time.sleep(60)


def get_repo_info(url):
    # extrair owner e repo
    parts = url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    while True:
        resp = session.get(api_url, timeout=20)
        if resp.status_code == 403:
            esperar_por_rate_limit(resp)
            continue
        if resp.status_code != 200:
            print(f"⚠️ Erro ao buscar {url}: {resp.status_code}")
            return {}

        data = resp.json()

        # dados do dono/org
        owner_data = {}
        try:
            resp_owner = session.get(data["owner"]["url"], timeout=20)
            if resp_owner.status_code == 200:
                owner_data = resp_owner.json()
        except Exception:
            pass

        return {
            "Estrelas": data.get("stargazers_count", 0),
            "Forks": data.get("forks_count", 0),
            "Última Atualização": data.get("updated_at", ""),
            "Linguagem Principal": data.get("language", ""),
            "País": owner_data.get("location", "")
        }


def main():
    df = pd.read_csv(INPUT_FILE)

    extra_data = []
    for _, row in df.iterrows():
        link = row["Link"]
        print(f"🔍 Buscando {link} ...")
        info = get_repo_info(link)
        extra_data.append(info)

    extra_df = pd.DataFrame(extra_data)
    df_final = pd.concat([df, extra_df], axis=1)

    df_final.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"✅ Arquivo enriquecido salvo em {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
