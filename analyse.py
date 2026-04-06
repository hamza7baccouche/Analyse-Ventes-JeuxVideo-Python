import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. CHARGEMENT DES DONNÉES
print("Chargement des données...")
df = pd.read_csv('vgsales.csv')

# 2. NETTOYAGE (Data Cleaning)
# On supprime les lignes où il manque des informations (années ou éditeurs)
df = df.dropna()

# 3. UTILISATION DE NUMPY (Statistiques rapides)
# On utilise NumPy pour extraire des informations globales sur les ventes
record_ventes = np.max(df['Global_Sales'])
moyenne_ventes = np.mean(df['Global_Sales'])

print("--- Statistiques Globales ---")
print(f"Record de ventes pour un jeu : {record_ventes} millions !")
print(f"Moyenne des ventes mondiales par jeu : {moyenne_ventes:.2f} millions")
print("---------------------------")

# 4. ANALYSE ET VISUALISATION
print("Création des graphiques en cours...")

# Configuration du style visuel
sns.set_theme(style="whitegrid")

# Graphique 1 : Top 10 des plateformes avec le plus de jeux
plt.figure(figsize=(10, 6))
top_platforms = df['Platform'].value_counts().head(10)
sns.barplot(x=top_platforms.index, y=top_platforms.values, palette="viridis")
plt.title('Top 10 des Plateformes avec le plus grand nombre de jeux')
plt.xlabel('Plateforme')
plt.ylabel('Nombre de jeux')
plt.savefig('graphique_plateformes.png') # Sauvegarde l'image
plt.show()

# Graphique 2 : Ventes globales par genre de jeu
plt.figure(figsize=(12, 6))
sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
sns.barplot(x=sales_by_genre.index, y=sales_by_genre.values, palette="rocket")
plt.title('Ventes mondiales totales par Genre de jeu (en millions)')
plt.xlabel('Genre')
plt.ylabel('Ventes (Millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graphique_ventes.png') # Sauvegarde l'image
plt.show()

print("Analyse terminée ! Les graphiques ont été sauvegardés.")