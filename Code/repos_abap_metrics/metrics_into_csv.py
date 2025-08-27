import os
import json
import csv

PASTA_RESULTADOS = "../Code/repos_abap_metrics/resultados"
CSV_SAIDA = "../Code/repos_abap_metrics/abaplint_consolidado.csv"


def consolidar_jsons():
    linhas = []

    for arquivo in os.listdir(PASTA_RESULTADOS):
        if not arquivo.endswith(".json"):
            continue

        repo = arquivo.replace(".json", "")
        caminho = os.path.join(PASTA_RESULTADOS, arquivo)

        with open(caminho, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Erro ao ler {arquivo}, ignorando...")
                continue

        issues = data.get("issues", [])
        for issue in issues:
            linhas.append({
                "repo": repo,
                "filename": issue.get("filename", ""),
                "key": issue.get("key", ""),
                "message": issue.get("message", ""),
                "severity": issue.get("severity", ""),
                "start_row": issue.get("start", {}).get("row", ""),
                "start_col": issue.get("start", {}).get("col", ""),
                "end_row": issue.get("end", {}).get("row", ""),
                "end_col": issue.get("end", {}).get("col", "")
            })

    # Salvar em CSV
    with open(CSV_SAIDA, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            "repo", "filename", "key", "message", "severity",
            "start_row", "start_col", "end_row", "end_col"
        ])
        writer.writeheader()
        writer.writerows(linhas)

    print(f"CSV consolidado gerado em {CSV_SAIDA} com {len(linhas)} issues.")

if __name__ == "__main__":
    consolidar_jsons()
