# Analyse des ventes — Atelier S08, Partie B

## Objectif
Consolider les ventes des régions Nord, Sud et Ouest.

## Organisation
- data/brut/ : fichiers CSV d'origine
- data/propre/ : données consolidées
- src/consolider.py : fusion et nettoyage
- src/resume.py : rapport des ventes
- resultats/resume.txt : résumé final

## Traitements
- Fusion des trois régions
- Suppression de 2 doublons exacts
- Ajout de la colonne region
- Calcul du chiffre_affaires
- Conservation des valeurs manquantes

## Résultats
- 171 lignes initiales
- 169 ventes conservées
- 37 110,60 € de chiffre d'affaires

## Exécution
1. Installer les dépendances :
   python -m pip install -r requirements.txt

2. Consolider :
   python src/consolider.py

3. Générer le résumé :
   python src/resume.py
