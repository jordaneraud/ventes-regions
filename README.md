# Analyse des ventes par région

Projet de formation Data Analyst (S08) : consolider les ventes des régions Nord, Sud et Ouest et produire un résumé des ventes.

## Fonctionnement

Le traitement principal rassemble les trois CSV, ajoute la région, supprime les doublons exacts, convertit les dates et valeurs numériques puis calcule le chiffre d'affaires. Les valeurs manquantes sont conservées.

Résultats enregistrés : 171 lignes initiales, 169 ventes conservées et 37 110,60 € de chiffre d'affaires.

## Installation et exécution

Depuis la racine du projet, avec Python 3 et un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/consolider.py
.\.venv\Scripts\python.exe src/resume.py
```

Ces deux scripts régénèrent respectivement les données consolidées et le résumé. Les dépendances sont figées dans requirements.txt.

## Structure

- `data/brut/` : ventes sources des trois régions.
- `data/propre/ventes_consolidees.csv` : données consolidées.
- `src/consolider.py` : consolidation et calcul du chiffre d'affaires.
- `src/resume.py` : synthèse par région et principaux produits.
- `resultats/resume.txt` : résumé enregistré.
- `src/inspecter.py`, `src/nettoyer.py`, `src/rapport.py` : scripts d'un autre parcours de traitement, prévus pour des CSV directement dans `data/` ; ils ne font pas partie de la procédure principale ci-dessus.
- `demonstrations-git/` : supports pédagogiques de restauration, branches et conflits.
- `livrables-s08/` : preuves locales, exclues du suivi Git.

## Outils et limites

Python, pandas, NumPy et Git. Les autres dépendances Python figurent dans requirements.txt.
Les libellés de produits ne sont pas uniformisés ; les regroupements distinguent donc les variantes de casse. Ce dépôt constitue un exercice de formation.

## Vérification des résultats

Après exécution du parcours principal, le résumé doit présenter 169 ventes et un chiffre d'affaires total de 37 110,60 €.

| Région | Chiffre d'affaires |
| --- | ---: |
| Nord | 12 771,00 € |
| Ouest | 13 803,60 € |
| Sud | 10 536,00 € |

Comparer ces valeurs avec `resultats/resume.txt` après régénération. Les CSV bruts restent la référence pour contrôler le traitement.
