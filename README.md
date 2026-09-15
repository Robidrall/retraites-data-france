# 📊 Retraites Data France : Radiographie d'un système

Ce dépôt a pour but d'analyser objectivement le système de retraite français par répartition face au défi démographique, et de modéliser les alternatives (capitalisation). Portée par une approche de Data Engineering, la méthodologie est 100% open data et reproductible. L'objectif est d'élever le niveau du débat public en sortant des postures idéologiques pour revenir à la rigueur arithmétique.

## 📦 Modules du projet

Ce dépôt est structuré de manière modulaire. Chaque dossier contient son propre jeu de données, ses scripts d'analyse et ses visualisations.

* 📁 **`01_repartition_vs_demographie`** : Analyse de l'effet ciseau (actifs vs retraités) de 1950 à 2100 et impact historique de la non-mise en place de la loi Thomas (1997).

## 🏛️ Sources des données

Toutes les analyses reposent sur des séries statistiques publiques officielles et incontestables. Aucun chiffre n'est inventé, tout est sourcé :

* **DREES** (Direction de la recherche, des études, de l'évaluation et des statistiques) : Effectifs historiques des retraités et des cotisants.
* **INSEE** (Institut national de la statistique et des études économiques) : Projections démographiques et séries d'emploi.
* **COR** (Conseil d'orientation des retraites) : Hypothèses macroéconomiques et projections du ratio de dépendance.

## ⚙️ Installation et Exécution

Pour cloner ce projet et reproduire les graphiques sur votre machine, assurez-vous d'avoir Python 3.9+ installé.

1. Clonez le dépôt :
```bash
git clone https://github.com/robidrall/retraites-data-france.git
cd retraites-data-france
```

2. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

3. Exécutez le script d'un module (exemple pour le module 01) :
```bash
cd 01_repartition_vs_demographie
python run.py
```
Le script lira les données CSV locales et générera le graphique haute résolution dans le même dossier.

## 💡 Philosophie

*In Data We Trust.* 
Ce code est publié sous licence open-source (MIT). Vous êtes libres de le forker, de l'améliorer, de vérifier les calculs et de partager les visualisations générées pour alimenter le débat public.