import csv

ARQUIVO_ENTRADA = "repos_abap.csv"
ARQUIVO_SAIDA = "repos_abap_sorted.csv"

def ordenar_csv_por_tamanho():
    print("Lendo CSV...")

    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        repos = []
        for row in reader:
            try:
                nome, tamanho, link, criado = row
                tamanho_int = int(tamanho) if tamanho.isdigit() else 0
                repos.append([nome, tamanho_int, link, criado])
            except:
                continue

    print("Ordenando...")

    repos.sort(key=lambda x: x[1], reverse=True)

    with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(repos)

    print(f"Arquivo {ARQUIVO_SAIDA} gerado.")

if __name__ == "__main__":
    ordenar_csv_por_tamanho()
