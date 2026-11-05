import pandas as pd
from pathlib import Path

fichiers = sorted(Path("data").glob("*.csv"))
tables = []

for fichier in fichiers:
    df = pd.read_csv(fichier, sep=None, engine="python")
    df["source"] = fichier.name
    tables.append(df)

ventes = pd.concat(tables, ignore_index=True)

print("Lignes avant nettoyage :", len(ventes))

ventes["date_vente"] = pd.to_datetime(ventes["date_vente"], errors="coerce")
ventes["quantite"] = pd.to_numeric(ventes["quantite"], errors="coerce")
ventes["prix_unitaire"] = pd.to_numeric(ventes["prix_unitaire"], errors="coerce")

doublons = ventes.duplicated(subset=["id_vente"]).sum()
print("Identifiants de vente en double :", doublons)

ventes = ventes.drop_duplicates(subset=["id_vente"], keep="first").copy()

ventes["montant"] = ventes["quantite"] * ventes["prix_unitaire"]

Path("resultats").mkdir(exist_ok=True)
ventes.to_csv("resultats/ventes_nettoyees.csv", index=False, encoding="utf-8-sig")

print("Lignes après nettoyage :", len(ventes))
print("Montant total :", round(ventes["montant"].sum(), 2), "€")
print("Villes manquantes :", ventes["ville"].isna().sum())
print("Fichier créé : resultats/ventes_nettoyees.csv")
