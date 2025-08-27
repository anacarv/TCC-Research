import pandas as pd

INPUT_FILE = "./Code/repos_abap_fetch/repos_abap_sorted.csv"
OUTPUT_FILE = "./Code/repos_abap_fetch/repos_abap_filtered.csv"

df = pd.read_csv(INPUT_FILE)

EXCLUDE_KEYWORDS = [
    # S/4HANA
    "s4hana", "hana", "fiori", "ui5", "sapui5", "openui5", "cds",
    "core data services", "ddls", "rap", "odata", "rest", "srv", "srvapi",
    "cloud", "btp", "hdb", "xsjs", "xsodata", "gateway",

    # Apresentações
    "presentation", "presentations", "slides", "slide", "talk", "session",
    "conference", "conf", "meetup", "summit", "symposium", "workshop", "webinar",

    # Exemplos
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


mask = df.apply(lambda row: row.astype(str).str.contains("|".join(EXCLUDE_KEYWORDS), case=False).any(), axis=1)
df_filtered = df[~mask]

df_filtered = df_filtered.sort_values(by="Tamanho (KB)", ascending=False)

df_filtered.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"CSV filtrado salvo em: {OUTPUT_FILE}")
