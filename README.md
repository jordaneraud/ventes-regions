# Analyse des ventes — Atelier S08

## Objectif
Fusionner et nettoyer les ventes de trois régions.

## Données
- ventes_nord.csv
- ventes_sud.csv
- ventes_ouest.csv

## Traitements
- Fusion des trois fichiers CSV
- Suppression de 3 doublons exacts
- Conversion des dates et des valeurs numériques
- Calcul du montant : quantité × prix unitaire
- Conservation des villes manquantes

## Résultats
- 171 lignes initiales
- 168 ventes conservées
- Chiffre d'affaires : 36 723,60 €
- 2 villes manquantes

## Exécution
Installer les dépendances :
python -m pip install -r requirements.txt

Lancer les scripts :
python src/inspecter.py
python src/nettoyer.py
python src/rapport.py

## Fichiers produits
- resultats/ventes_nettoyees.csv
- resultats/rapport_categories.csv
