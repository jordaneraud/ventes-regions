import pandas as pd
from pathlib import Path

tables = []

for region in ["nord", "sud", "ouest"]:
    fichier = Path(f"data/brut/ventes_{region}.csv")
    df = pd.read_csv(fichier, sep=None, engine="python")
    df["region"] = region
    tables.append(df)

ventes = pd.concat(tables, ignore_index=True)

print("Lignes initiales :", len(ventes))

doublons = ventes.duplicated().sum()
print("Doublons exacts :", doublons)

ventes = ventes.drop_duplicates().copy()

ventes["date_vente"] = pd.to_datetime(
    ventes["date_vente"], errors="coerce"
)
ventes["quantite"] = pd.to_numeric(
    ventes["quantite"], errors="coerce"
)
ventes["prix_unitaire"] = pd.to_numeric(
    ventes["prix_unitaire"], errors="coerce"
)

ventes["chiffre_affaires"] = (
    ventes["quantite"] * ventes["prix_unitaire"]
)

Path("data/propre").mkdir(exist_ok=True)

ventes.to_csv(
    "data/propre/ventes_consolidees.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Lignes conservées :", len(ventes))
print("CA total :", round(ventes["chiffre_affaires"].sum(), 2), "€")
print("Fichier consolidé créé.")
