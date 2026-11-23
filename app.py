import pandas as pd
import plotly.express as px

données = pd.read_csv('ventes.csv')
données['chiffre_affaires'] = données['qte'] * données['prix']

# Gráfico de ejemplo: ventas por región
fig_region = px.pie(données, values='qte', names='region', title='Quantité vendue par région')
fig_region.write_html('ventes-par-region.html')

# 1. Gráfico de ventas (cantidad) por producto
fig_produit = px.bar(données, x='produit', y='qte', title='Ventes par produit')
fig_produit.write_html('ventes-par-produit.html')

# 2. Gráfico de chiffre d'affaires por producto
fig_ca = px.bar(données, x='produit', y='chiffre_affaires', title="Chiffre d'affaires par produit")
fig_ca.write_html('chiffre-affaires-par-produit.html')

print("Gráficos generados con éxito.")
