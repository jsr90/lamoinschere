# ⛽ LaMoinsChère

## Description
LaMoinsChère est une application Streamlit qui permet de trouver les stations-service les moins chères dans un département donné en France, en fonction du type de carburant sélectionné.

## Fonctionnalités
- Sélection d'un département parmi une liste.
- Sélection d'un type de carburant (Gazole, SP98, SP95, E10, E85, GPLc).
- Affichage des 30 stations-service les moins chères pour le carburant choisi dans le département sélectionné.

## Prérequis
- Python 3.7 ou supérieur
- Bibliothèques Python :
  - `streamlit`
  - `requests`
  - `pandas`

## Installation
1. Clonez ce dépôt ou téléchargez les fichiers.
2. Installez les dépendances nécessaires avec la commande :
   ```bash
   pip install -r requirements.txt
   ```
3. Assurez-vous que le fichier `departements-region.json` est présent dans le même répertoire que `app.py`.

## Utilisation
1. Lancez l'application Streamlit avec la commande :
   ```bash
   streamlit run app.py
   ```
2. Ouvrez l'application dans votre navigateur et suivez les instructions pour sélectionner un département et un type de carburant.

## Sources de données
Les données sur les prix des carburants proviennent de l'API du gouvernement français :
[https://data.economie.gouv.fr](https://data.economie.gouv.fr)

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.
