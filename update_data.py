import json
import urllib.request
from datetime import datetime

# 1. URL de l'API publique (Coindesk pour le prix du Bitcoin en temps réel)
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    # Connexion à l'API et téléchargement des données brutes
    with urllib.request.urlopen(url) as response:
        source_de_donnees = response.read().decode()
        
    # Transformation du texte brut en dictionnaire Python (Parsing JSON)
    donnees_api = json.loads(source_de_donnees)
    
    # Extraction précise du prix du Bitcoin en USD (ex: "65,420.12")
    prix_btc = donnees_api["bpi"]["USD"]["rate"] + " USD"
    
    # Récupération de l'heure actuelle sur le serveur
    heure_actuelle = datetime.now().strftime("%H:%M")

    # 2. Reconstruction de la structure de NOTRE fichier data.json
    nouvelles_donnees = {
        "titre_flux": "Flux de données Lytechubedi (LIVE API)",
        "derniere_mise_a_jour": heure_actuelle,
        "valeur_crypto": prix_btc,
        "statut_reseau": "Opérationnel",
        "nombre_alertes": 0
    }

    # 3. Écrasement automatique du fichier data.json avec les vraies valeurs
    with open("data.json", "w", encoding="utf-8") as fichier:
        json.dump(nouvelles_donnees, fichier, ensure_ascii=False, indent=4)
        
    print("Succès : Le fichier data.json a été mis à jour avec les données de l'API.")

except Exception as error:
    print(f"Erreur critique lors de la récupération de l'API : {error}")

