import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# 1. CHARGEMENT DES DONNÉES DEPUIS LE CSV
# =============================================================================
# Ce fichier contient la consolidation des séries longues de la DREES,
# de l'Insee (projections 2021-2070 prolongées) et du COR.
csv_file = "retraites_repartition_france_1950_2070_complet.csv"
df = pd.read_csv(csv_file)

# Extraction dynamique des valeurs clés pour peupler automatiquement
# les "Stat Cards" (KPI) situées en haut du tableau de bord.
val_1950_ratio = df[df["annee"] == 1950]["ratio_cotisants_retraite"].values[0]
val_1950_eff = df[df["annee"] == 1950]["effort_cotisation_50pct"].values[0]

val_2026_ratio = df[df["annee"] == 2026]["ratio_cotisants_retraite"].values[0]
val_2026_eff = df[df["annee"] == 2026]["effort_cotisation_50pct"].values[0]

val_2070_ratio = df[df["annee"] == 2070]["ratio_cotisants_retraite"].values[0]
val_2070_eff = df[df["annee"] == 2070]["effort_cotisation_50pct"].values[0]

# =============================================================================
# 2. CONFIGURATION DE LA DIRECTION ARTISTIQUE (THEME "SOBER DARK")
# =============================================================================
# Palette de couleurs optimisée pour un rendu pro (type GitHub Dark / Vercel)
BG_COLOR = "#0D1117"        # Fond principal (gris-bleu très sombre)
PANEL_BG = "#161B22"        # Fond légèrement plus clair pour les cartes KPI
GRID_COLOR = "#30363D"      # Couleur des bordures et de la grille
TEXT_MAIN = "#E6EDF3"       # Texte principal ultra lisible
TEXT_MUTED = "#8B949E"      # Texte secondaire (légendes, axes)
COT_COLOR = "#58A6FF"       # Bleu clair pour la ligne des cotisants
RET_COLOR = "#F85149"       # Rouge alerte pour la ligne des retraités
WARN_COLOR = "#D29922"      # Or / Ambre pour mettre en valeur 1997

# Choix d'une police sans serif claire et moderne
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

# Création de la figure (Format 16:9 idéal pour Twitter/X)
fig = plt.figure(figsize=(15, 8.5), dpi=300)
fig.patch.set_facecolor(BG_COLOR)

# Utilisation de GridSpec pour diviser l'image en 2 zones :
# - Ligne du haut (ratio 0.28) : 3 colonnes pour les KPI
# - Ligne du bas (ratio 1.0) : Le graphique principal
gs = fig.add_gridspec(2, 3, height_ratios=[0.28, 1.0], hspace=0.25, wspace=0.2)

# =============================================================================
# 3. CRÉATION DES 3 CARTES KPI (EN HAUT)
# =============================================================================
# Données à afficher dans chaque carte : (Titre, Valeur 1, Valeur 2, Sous-titre, Couleur)
kpis = [
    ("1950 • ORIGINE DU MODÈLE", f"{val_1950_ratio:.1f} actifs", "pour 1 retraité", f"Cotisation théorique : {val_1950_eff:.0f}%", COT_COLOR),
    ("2026 • SITUATION ACTUELLE", f"{val_2026_ratio:.2f} actifs", "pour 1 retraité", f"Cotisation théorique : ~{val_2026_eff:.0f}%", WARN_COLOR),
    ("2070 • TRAJECTOIRE PROJETÉE", f"{val_2070_ratio:.2f} actif", "pour 1 retraité", f"Cotisation théorique : >{val_2070_eff:.0f}%", RET_COLOR)
]

# Boucle pour générer les 3 cartes
for i, (titre, val, subval, desc, color) in enumerate(kpis):
    ax_card = fig.add_subplot(gs[0, i])
    ax_card.set_facecolor(PANEL_BG)
    ax_card.axis("off") # On cache les axes classiques pour dessiner nos propres boîtes
    
    # 3.1 Boîte de fond avec bordure discrète
    rect = plt.Rectangle((0, 0), 1, 1, transform=ax_card.transAxes, 
                         facecolor=PANEL_BG, edgecolor=GRID_COLOR, lw=1, clip_on=False)
    ax_card.add_patch(rect)
    
    # 3.2 Petit liseré de couleur en haut de la carte
    bar = plt.Rectangle((0, 0.96), 1, 0.04, transform=ax_card.transAxes, facecolor=color, clip_on=False)
    ax_card.add_patch(bar)
    
    # 3.3 Insertion des textes
    ax_card.text(0.06, 0.75, titre, transform=ax_card.transAxes, fontsize=9, fontweight="bold", color=TEXT_MUTED)
    
    # La valeur centrale est placée à gauche (x=0.06), et la mention "pour 1 retraité" 
    # est placée plus à droite (x=0.55) pour éviter que les mots ne se chevauchent.
    ax_card.text(0.06, 0.40, val, transform=ax_card.transAxes, fontsize=18, fontweight="bold", color=TEXT_MAIN)
    ax_card.text(0.55, 0.42, subval, transform=ax_card.transAxes, fontsize=10, color=TEXT_MUTED)
    
    ax_card.text(0.06, 0.15, desc, transform=ax_card.transAxes, fontsize=9.5, color=color, fontweight="bold")

# =============================================================================
# 4. CRÉATION DU GRAPHIQUE CENTRAL (L'EFFET CISEAU)
# =============================================================================
ax_hero = fig.add_subplot(gs[1, :])
ax_hero.set_facecolor(BG_COLOR)

# Nettoyage des bordures (on garde uniquement gauche et bas)
for spine in ax_hero.spines.values():
    spine.set_color(GRID_COLOR)
    spine.set_linewidth(1)
ax_hero.spines["top"].set_visible(False)
ax_hero.spines["right"].set_visible(False)

# Ajout d'une grille discrète en arrière-plan (zorder=1)
ax_hero.grid(True, linestyle="--", color=GRID_COLOR, alpha=0.7, zorder=1)
ax_hero.tick_params(colors=TEXT_MUTED, labelsize=9)

# 4.1 Remplissage des zones entre les deux courbes (Effet visuel du Ciseau)
# La zone bleue (1950-2026) représente la marge de sécurité historique
ax_hero.fill_between(
    df["annee"], df["cotisants_millions"], df["retraites_millions"],
    where=(df["annee"] <= 2026), color=COT_COLOR, alpha=0.10, zorder=2,
    label="Marge de sécurité démographique (1950 - 2026)"
)
# La zone rouge (2026-2070) montre l'étranglement financier futur
ax_hero.fill_between(
    df["annee"], df["cotisants_millions"], df["retraites_millions"],
    where=(df["annee"] >= 2026), color=RET_COLOR, alpha=0.08, zorder=2,
    label="Zone de fermeture du ciseau (Étranglement financier)"
)

# Séparation des données pour styliser différemment le passé (ligne pleine) 
# et le futur (ligne pointillée)
df_hist = df[df["annee"] <= 2026]
df_proj = df[df["annee"] >= 2026]

# 4.2 Tracé des lignes (Cotisants = Bleu, Retraités = Rouge)
ax_hero.plot(df_hist["annee"], df_hist["cotisants_millions"], color=COT_COLOR, lw=3.5, label="Cotisants (actifs en emploi)", zorder=4)
ax_hero.plot(df_proj["annee"], df_proj["cotisants_millions"], color=COT_COLOR, lw=2.5, ls="--", zorder=4)

ax_hero.plot(df_hist["annee"], df_hist["retraites_millions"], color=RET_COLOR, lw=3.5, label="Retraités de droit direct", zorder=4)
ax_hero.plot(df_proj["annee"], df_proj["retraites_millions"], color=RET_COLOR, lw=2.5, ls="--", zorder=4)

# =============================================================================
# 5. AJOUT DES ANNOTATIONS ET REPÈRES HISTORIQUES
# =============================================================================

# 5.1 Réformes paramétriques (Affichées très discrètement en arrière-plan)
reperes = [
    (1982, "1982 : 60 ans"),
    (1993, "1993 : Balladur"),
    (2010, "2010 : 62 ans"),
    (2023, "2023 : 64 ans"),
]
for annee, label_ref in reperes:
    # Ligne verticale pointillée (zorder=3 pour passer derrière les lignes principales)
    ax_hero.axvline(annee, color=GRID_COLOR, ls=":", lw=1.2, zorder=3)
    # Texte tourné à 90 degrés placé près de l'axe X (y=2.5)
    ax_hero.text(annee, 2.5, f" {label_ref}", rotation=90, color=TEXT_MUTED, fontsize=7.5, va="bottom", zorder=3)

# 5.2 Ligne du PIVOT actuel (2026)
ax_hero.axvline(2026, color=TEXT_MUTED, lw=1.5, ls="--", zorder=5)
ax_hero.text(2028, 33, "2026 : PIVOT ACTUEL", color=TEXT_MAIN, fontsize=9, fontweight="bold")

# 5.3 L'occasion manquée : Loi Thomas de 1997
# Cette annotation est le cœur du message, on force le zorder très haut (10 et 12) 
# pour qu'elle s'affiche par-dessus absolument tout (zones, lignes, grilles).
ax_hero.axvline(1997, color=WARN_COLOR, lw=1.5, ls="-", zorder=8)
cot_97 = df[df["annee"] == 1997]["cotisants_millions"].values[0]
ret_97 = df[df["annee"] == 1997]["retraites_millions"].values[0]

# Points marquant l'écart
ax_hero.scatter([1997, 1997], [cot_97, ret_97], color=WARN_COLOR, s=60, zorder=10, edgecolor=BG_COLOR, lw=1.5)

# Encadré textuel explicatif
ax_hero.annotate(
    "1997 : Abrogation de la Loi Thomas\nL'écart était de +12 millions d'actifs.\nLe point idéal pour la capitalisation.",
    xy=(1997, (cot_97 + ret_97) / 2), # La flèche pointe au centre de l'écart
    xytext=(2003, 14),                # Position de la boîte de texte
    fontsize=9.5,
    fontweight="bold",
    color=WARN_COLOR,
    zorder=12,
    bbox=dict(boxstyle="round,pad=0.6", facecolor=PANEL_BG, edgecolor=GRID_COLOR, lw=1),
    arrowprops=dict(arrowstyle="->", color=WARN_COLOR, lw=1.5)
)

# =============================================================================
# 6. FINITIONS DU GRAPHIQUE (TITRES, LÉGENDES ET SAUVEGARDE)
# =============================================================================
ax_hero.set_ylabel("Effectifs cumulés (Millions de personnes)", color=TEXT_MUTED, fontsize=10)
ax_hero.set_xlabel("Année (1950 - 2070)", color=TEXT_MUTED, fontsize=10)
ax_hero.set_xlim(1948, 2102)
ax_hero.set_ylim(0, 37)

# Légende placée en haut à gauche
ax_hero.legend(loc="upper left", facecolor=BG_COLOR, edgecolor=GRID_COLOR, labelcolor=TEXT_MAIN, fontsize=9)

# Titre général du tableau de bord (placé au niveau de la figure, pas de l'axe)
fig.text(0.06, 0.95, "RETRAITES EN FRANCE : L'EFFET CISEAU QUI CONDAMNE LA RÉPARTITION", fontsize=16, fontweight="bold", color=TEXT_MAIN)
fig.text(0.06, 0.92, "Sources : DREES, Insee, COR (Modélisation Samuelson).", fontsize=10, color=TEXT_MUTED)

# Sauvegarde de l'image en haute résolution (300 dpi)
output_file = "hero_ciseau_retraite_2026_sober.png"
fig.savefig(output_file, dpi=300, bbox_inches="tight")
print(f"Graphique généré avec succès : {output_file}")