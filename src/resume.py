import pandas as pd
from pathlib import Path

df = pd.read_csv("data/propre/ventes_consolidees.csv")

ca_region = df.groupby("region")["chiffre_affaires"].sum()
top_produits = (
    df.groupby("produit")["chiffre_affaires"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

lignes = [
    "=== RÉSUMÉ DES VENTES ===",
    "",
    f"Nombre de ventes : {len(df)}",
    f"Chiffre d'affaires total : {df['chiffre_affaires'].sum():.2f} €",
    "",
    "=== CA PAR RÉGION ===",
    ca_region.round(2).to_string(),
    "",
    "=== TOP 5 DES PRODUITS ===",
    top_produits.round(2).to_string()
]

rapport = "\n".join(lignes)

Path("resultats").mkdir(exist_ok=True)
Path("resultats/resume.txt").write_text(rapport, encoding="utf-8")

print(rapport)
print("\nFichier créé : resultats/resume.txt")
