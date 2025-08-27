import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../Code/repos_abap_metrics/abaplint_consolidado.csv")

metricas = df.groupby("repo").agg(
    num_issues_total=("key", "count"),
    num_erros=("severity", lambda x: (x == "error").sum()),
    num_warnings=("severity", lambda x: (x == "warning").sum()),
    num_infos=("severity", lambda x: (x == "info").sum()),
    num_tipos_unicos=("key", pd.Series.nunique)
).reset_index()

print("Métricas extraídas:")
print(metricas.head())

# MinMaxScaler scikit-learn
colunas_metricas = [c for c in metricas.columns if c.startswith("num_")]

scaler = MinMaxScaler()
metricas_normalizadas = metricas.copy()
metricas_normalizadas[colunas_metricas] = scaler.fit_transform(metricas[colunas_metricas])

metricas_normalizadas.to_csv("metricas_normalizadas.csv", index=False, encoding="utf-8-sig")
print("Arquivo 'metricas_normalizadas.csv' salvo (todas as métricas normalizadas).")

corr = metricas_normalizadas[colunas_metricas].corr(method="pearson")
print("\nMatriz de correlação:")
print(corr)

limite_corr = 0.9
descartar = set()

for i in range(len(colunas_metricas)):
    for j in range(i + 1, len(colunas_metricas)):
        if abs(corr.iloc[i, j]) > limite_corr:
            descartar.add(colunas_metricas[j])

print(f"\nMétricas redundantes descartadas: {descartar}")

metricas_final = metricas_normalizadas.drop(columns=list(descartar))
metricas_final.to_csv("metricas_final.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'metricas_final.csv' salvo (sem métricas redundantes).")
