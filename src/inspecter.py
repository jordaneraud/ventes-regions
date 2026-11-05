import pandas as pd
from pathlib import Path

for fichier in Path("data").glob("*.csv"):
    print(f"\n===== {fichier.name} =====")
    df = pd.read_csv(fichier, sep=None, engine="python")
    print("Dimensions :", df.shape)
    print("Colonnes :", df.columns.tolist())
    print(df.head(3).to_string(index=False))
    print("Valeurs manquantes :", df.isna().sum().to_dict())
