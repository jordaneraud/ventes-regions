import pandas as pd

df = pd.read_csv("resultats/ventes_nettoyees.csv")

print("\n=== VENTES PAR CATÉGORIE ===")
print(df.groupby("categorie")["montant"].sum().round(2).to_string())

print("\n=== VENTES PAR VILLE ===")
print(df.groupby("ville", dropna=False)["montant"].sum().round(2).to_string())

print("\n=== BILAN ===")
print("Nombre de ventes :", len(df))
print("Chiffre d'affaires :", round(df["montant"].sum(), 2), "€")

df.groupby("categorie", as_index=False)["montant"].sum().to_csv(
    "resultats/rapport_categories.csv", index=False
)

print("\nRapport enregistré dans resultats/rapport_categories.csv")
