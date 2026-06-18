import json
import urllib.request
import urllib.parse
from datetime import datetime

url = "https://dummyjson.com/products?limit=30"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        source_brute = response.read().decode()
        
    donnees_api = json.loads(source_brute)
    liste_produits = donnees_api.get("products", [])
    
    # Tri algorithmique des produits
    produits_tries = sorted(liste_produits, key=lambda x: (x.get("rating", 0), x.get("discountPercentage", 0)), reverse=True)
    
    # SÉLECTION : On extrait le TOP 5 complet
    top_5 = produits_tries[:5]
    
    liste_finale = []
    for produit in top_5:
        nom_produit = produit.get("title", "Produit inconnu")
        niche = produit.get("category", "Général").capitalize()
        prix = f"{produit.get('price', 0)} USD"
        note = produit.get("rating", 4.5)
        stock_restant = produit.get("stock", 10)
        image_url = produit.get("thumbnail", "")
        
        nom_encode = urllib.parse.quote(nom_produit)
        lien_sourcing = f"https://www.google.com/search?q={nom_encode}+sourcing+aliexpress"
        
        score_viralite = min(100, int((note * 15) + (100 - stock_restant) * 0.25))
        
        # On ajoute le produit au catalogue du jour
        liste_finale.append({
            "niche": niche,
            "nom": nom_produit,
            "prix": prix,
            "score": f"Viral à {score_viralite}%",
            "url_image": image_url,
            "url_produit": lien_sourcing
        })
        
    heure_actuelle = datetime.now().strftime("%H:%M")

    # Structure JSON propre contenant le tableau de produits
    nouvelles_donnees = {
        "derniere_mise_a_jour": heure_actuelle,
        "produits": liste_finale
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(nouvelles_donnees, f, indent=4, ensure_ascii=False)
        
    print("Fichier data.json mis à jour avec le Top 5 des produits !")

except Exception as e:
    print(f"Erreur : {e}")
    exit(1)
