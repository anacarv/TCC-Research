import csv
import os
import subprocess

CSV_REPOS = os.path.join(os.path.dirname(__file__), "./Code/repos_abap_fetch/repos_abap_filtered.py")
PASTA_REPOS = "./Code/repos_abap_metrics/repositorios"
PASTA_RESULTADOS = "./Code/repos_abap_metrics/resultados"

os.makedirs(PASTA_REPOS, exist_ok=True)
os.makedirs(PASTA_RESULTADOS, exist_ok=True)

# Palavras-chave que devem excluir o repo se aparecerem no README ou nome
EXCLUDE_KEYWORDS = [
    # S/4HANA e tecnologias modernas
    "s4hana", "hana", "fiori", "ui5", "sapui5", "openui5", "cds",
    "core data services", "ddls", "rap", "odata", "rest", "srv", "srvapi",
    "cloud", "btp", "hdb", "xsjs", "xsodata", "gateway",

    # Apresentações/eventos
    "presentation", "presentations", "slides", "slide", "talk", "session",
    "conference", "conf", "meetup", "summit", "symposium", "workshop", "webinar",

    # Exemplos/demonstração
    "example", "examples", "sample", "samples", "demo", "demos",
    "playground", "sandbox", "tutorial", "training", "learn", "learning",
    "edu", "education", "academy", "course", "class",

    # Documentação/utilitários
    "docs", "documentation", "doc", "generator", "template", "templates",
    "scaffold", "boilerplate", "skeleton", "mock", "mockup", "fake",
    "testdata", "testing", "unittest", "ci", "cd",

    # Integrações externas
    "api", "graphql", "restapi", "integration", "connector", "adapter",
    "docker", "k8s", "kubernetes", "helm", "python", "java", "node",
    "javascript", "typescript",

    # Miscelânea
    "personal", "blog", "notes", "articles", "paper", "book", "ebook",
    "magazine", "experiment", "experiments", "research", "prototype",
    "lab", "misc", "etc", "stuff"
]


def contem_palavra_proibida(texto: str) -> bool:
    texto_lower = texto.lower()
    return any(palavra in texto_lower for palavra in EXCLUDE_KEYWORDS)


def clonar_repositorio(nome, url):
    destino = os.path.join(PASTA_REPOS, nome)
    if not os.path.exists(destino):
        print(f"Clonando {nome}...")
        try:
            subprocess.run(["git", "clone", url, destino], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao clonar {nome}: {e}")
            return None
    return destino


def encontrar_abap_files(pasta_repo):
    """Retorna lista de arquivos .abap dentro do repositório"""
    abap_files = []
    for root, _, files in os.walk(pasta_repo):
        for file in files:
            if file.lower().endswith(".abap"):
                abap_files.append(os.path.join(root, file))
    return abap_files


def readme_tem_palavra_proibida(pasta_repo):
    """Verifica se algum README contém palavras proibidas"""
    for file in os.listdir(pasta_repo):
        if file.lower().startswith("readme"):
            caminho = os.path.join(pasta_repo, file)
            try:
                with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                    conteudo = f.read()
                    if contem_palavra_proibida(conteudo):
                        return True
            except Exception:
                pass
    return False


def rodar_abaplint(nome, pasta_repo, abap_files):
    print(f"Rodando abaplint em {nome}...")
    saida_json = os.path.join(PASTA_RESULTADOS, f"{nome}.json")

    try:
        with open(saida_json, "w", encoding="utf-8") as f:
            subprocess.run(
                ["abaplint.cmd", "--format", "json", *abap_files],
                cwd=pasta_repo,
                stdout=f,
                stderr=subprocess.PIPE,
                check=False,
                text=True
            )
    except Exception as e:
        print(f"Erro ao rodar abaplint no repo {nome}: {e}")
        return None

    return saida_json


def main():
    with open(CSV_REPOS, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nome = row["Nome"]
            url = row["Link"]

            # filtro já pelo nome do repo
            if contem_palavra_proibida(nome):
                print(f"{nome} descartado (nome contém palavra proibida).")
                continue

            pasta_repo = clonar_repositorio(nome, url)
            if not pasta_repo:
                continue

            # filtro pelo README
            if readme_tem_palavra_proibida(pasta_repo):
                print(f"{nome} descartado (README contém palavra proibida).")
                continue

            # procura arquivos .abap
            abap_files = encontrar_abap_files(pasta_repo)
            if not abap_files:
                print(f"{nome} descartado (nenhum arquivo .abap encontrado).")
                continue

            resultado = rodar_abaplint(nome, pasta_repo, abap_files)
            if resultado:
                print(f"Resultado salvo em {resultado}")


if __name__ == "__main__":
    main()
