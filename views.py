from django.shortcuts import render
from django.http import JsonResponse

import requests
import json

# Select fields to show
fields = ['prix_valeur', 'adresse', 'cp', 'ville']
context = {}

# Open  json file with departements names
file = open('./lamoinschere/departements-region.json', 'r')
departements = json.load(file)

# Add dep names and carburant names to context dict
context['departements'] = departements
context['carburants'] = ["Gazole", "SP98", "SP95", "E10", "E85", "GPLc"]

# Index page returning index.html
def index(request):
    return render(request, 'lamoinschere/index.html', context=context)

# Search page returning json object with data from API
def search(request):
    
    if request.POST.get('action') == 'post':

        # Get department name and carburant from form
        dep_name = request.POST.get('dep_name')
        prix_nom = request.POST.get('prix_nom')

        # Call API to get json response
        response = requests.get(f"https://data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-instantane-test-ods-copie&q=&rows=100&start=0&sort=-prix_valeur&facet=prix_nom&facet=dep_name&refine.dep_name={dep_name}&refine.prix_nom={prix_nom}")
        records = response.json()['records']

        # Store items with needed fields
        items = {}
        i=0
        for record in records:
            items[i] = {}
            for field in fields:
                items[i][field] = record['fields'][field]
            i = i+1

        # Create a dictionary to return in JsonResponse
        dic = {}
        dic['dep_name'] = dep_name
        dic['prix_nom'] = prix_nom
        dic['items'] = items

        return JsonResponse(dic, safe=False)