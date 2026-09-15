# 01. Retraite par Répartition : L'Effet Ciseau Démographique (1950–2100)

Ce module documente et modélise l'évolution sur 150 ans du rapport démographique entre cotisants et retraités en France. Il met en lumière l'impasse arithmétique de la répartition pure face au vieillissement de la population, illustre l'impact des réformes paramétriques successives et analyse le coût d'opportunité historique de l'abrogation de la loi Thomas (fonds de pension) en 1997.

---

## 📊 Aperçu du visuel produit

Le script génère une infographie au format 16:9 haute résolution (`hero_ciseau_retraite_2026_v2.png`), conçue pour la diffusion sur X et les plateformes d'analyse économique.

* **Stat Cards (KPI) :** Comparatif direct entre 1950 (5 actifs/retraité), 2026 (1,68 actif/retraité) et 2100 (1,17 actif/retraité).
* **Effet ciseau en volumes :** Croisement des courbes d'actifs cotisants et de pensionnés de droit direct (en millions de personnes).
* **Marqueur 1997 :** Mise en évidence de l'abrogation de la loi Thomas, adoptée alors que le différentiel démographique était encore de +12 millions d'actifs.
* **Chronologie des réformes :** Repères verticaux des réformes paramétriques (1982, 1993, 2010, 2023).

---

## 📐 Modèle mathématique et Limites Macroéconomiques

L'illustration de l'effort contributif repose sur le théorème d'équilibre actuariel d'un régime par répartition pure (**théorème de Samuelson-Aaron**) :

$$\text{Masse des cotisations perçues} = \text{Masse des pensions versées}$$

Soit :
$$\tau_t \times N_t \times w_t = R_t \times p_t$$

Où :
* $\tau_t$ : taux de cotisation retraite effectif (part patronale + salariale).
* $N_t$ : nombre d'actifs cotisants.
* $w_t$ : salaire brut moyen.
* $R_t$ : nombre de retraités (pensions de droit direct).
* $p_t$ : pension moyenne brute.

En réarrangeant les termes pour exprimer le **taux de prélèvement d'équilibre** requis sur chaque travailleur :

$$\tau_t = \left( \frac{p_t}{w_t} \right) \times \left( \frac{R_t}{N_t} \right) = \frac{\text{Taux de remplacement}}{\text{Ratio démographique}}$$

### Implications empiriques (Hypothèse stricte) :
À taux de remplacement constant (calibré ici à titre normatif à **50 %** du salaire brut moyen pour isoler le choc démographique pur) :
* **1950 (Ratio = 5,00) :** $\tau = 10,0\%$ de cotisation théorique.
* **2026 (Ratio = 1,68) :** $\tau \approx 29,8\%$ de cotisation théorique.
* **2070 (Ratio = 1,25) :** $\tau = 40,0\%$ de cotisation théorique.

### ⚠️ Limites du modèle et "Triches" du système réel
Ce modèle est un *ceteris paribus* (toutes choses égales par ailleurs) conçu pour isoler la dérive démographique. Dans la réalité, le taux de prélèvement sur les fiches de paie n'explosera pas jusqu'à 40% car le système français absorbe déjà le choc autrement :

1. **La fiscalisation du système (Subventions de l'État) :** Le régime n'est plus financé uniquement par le travail. L'État compense le trou démographique par l'impôt (création de la CSG, affectation d'une partie de la TVA, taxes sectorielles). Le coût est transféré du salaire brut vers le pouvoir d'achat général.
2. **L'érosion du niveau de vie relatif des retraités :** Contrairement à l'hypothèse d'un taux de remplacement maintenu, l'État a désindexé les pensions des salaires pour les indexer sur les prix (inflation). Mathématiquement, le terme $\frac{p_t}{w_t}$ s'effondre lentement : les retraités s'appauvrissent structurellement par rapport aux actifs pour éviter la faillite.
3. **L'omission de la productivité (PIB) :** Le modèle brut occulte les gains de productivité et la croissance du PIB. Si un travailleur de 2070 produit beaucoup plus de valeur ajoutée qu'en 1950, une part de ce gain finance théoriquement le déséquilibre.

**Conclusion :** Si le système n'a pas encore fait faillite, ce n'est pas parce que la répartition fonctionne. C'est parce qu'il a été discrètement transformé en un **système de solidarité fiscalisé**, actant l'échec de son équation contributive originelle.

---

## 📁 Structure des fichiers

```text
01_repartition_vs_demographie/
│
├── README.md                                          # Documentation méthodologique
├── run.py                                             # Script d'exécution et génération du graphique
├── retraites_repartition_france_1950_2100_complet.csv # Jeu de données annuel complet (151 points)
└── hero_ciseau_retraite_2026_v2.png                   # Rendu visuel 16:9 haute définition

---

## 📚 Sources officielles & Données primaires

Le jeu de données `retraites_repartition_france_1950_2100_complet.csv` consolide les séries statistiques publiques suivantes :

1. **DREES (Direction de la recherche, des études, de l'évaluation et des statistiques) :**
   * Panoramas annuels *« Les retraités et les retraites »* (modèle de microsimulation **ANCETRE**, effectifs de retraités de droit direct, séries longues d'emploi cotisant).
   * Lien : [data.drees.sante.gouv.fr](https://data.drees.sante.gouv.fr/)
2. **COR (Conseil d'orientation des retraites) :**
   * Rapports annuels sur les évolutions et perspectives des retraites en France (scénario macroéconomique et démographique de référence).
   * Lien : [cor-retraites.fr/publications](https://www.cor-retraites.fr/publications)
3. **INSEE :**
   * Séries historiques de l'emploi intérieur et projections démographiques 2021–2070 (structure par âge et projections de population active).
   * Lien : [insee.fr/fr/statistiques/5893639](https://www.insee.fr/fr/statistiques/5893639)

> **Note méthodologique sur l'interpolation :** Les jalons statistiques quinquennaux et décennaux officiels sont reliés à l'aide d'une interpolation polynomiale monotone par morceaux (**PCHIP** - *Piecewise Cubic Hermite Interpolating Polynomial*), évitant tout artefact oscillatoire artificiel tout en garantissant la stricte fidélité aux dynamiques démographiques réelles.

---

## 🚀 Reproduction du graphique

### Prérequis
Installer les dépendances Python nécessaires :

```bash
pip install matplotlib pandas