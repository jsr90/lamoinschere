import streamlit as st
import requests
import json
import pandas as pd

columns_to_display = ['cp', 'adresse', 'ville', 'gazole_prix', 'sp98_prix', 'sp95_prix', 'e10_prix', 'e85_prix', 'gplc_prix']
carburants = ["Gazole", "SP98", "SP95", "E10", "E85", "GPLc"]

with open('departements-region.json', 'r', encoding='utf8') as file:
    departements_json = json.load(file)
    
departements = {}
for d in departements_json:
    value = d["dep_name"]
    key = str(d["num_dep"]) + ' - ' + d["dep_name"] + ' - ' + d["region_name"]
    departements[key] = value

st.title("⛽ LaMoinsChère")  # Ajout de l'icône de station-service

dep_name_key = st.selectbox(label='Choisissez le departement:', options=departements.keys())
dep_name_value = departements[dep_name_key]

carburant = st.selectbox(label='Choisissez le type de carburant:', options=carburants)
url = f'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?order_by={carburant.lower()}_prix&limit=30&&refine=carburants_disponibles%3A%22{carburant}%22&refine=departement%3A%22{dep_name_value}%22'
response = requests.get(url)
if response.status_code == 200:
    records = response.json()['results']
else:
    st.error("Erreur lors de la récupération des données.")
    records = []

table = pd.json_normalize(records)[columns_to_display]

st.dataframe(table, use_container_width=True, hide_index=True)
