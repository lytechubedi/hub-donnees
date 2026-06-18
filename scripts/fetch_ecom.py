import json
import urllib.request
import urllib.parse
from datetime import datetime

url = "https://dummyjson.com/products?limit=30"

try:
    # Connexion sécurisée à l'API de sourcing
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        source_brute = response.read().decode()
        
    donnees_api = json.loads(source_brute)
    liste_produits = donnees_api.get("products", [])
    
    # Tri des produits par note et réduction
    produits_tries = sorted(liste_produits, key=lambda x: (x.get("rating", 0), x.get("discountPercentage", 0)), reverse=True)
    top_5 = produits_tries[:5]
    
    liste_finale = []
    for p in top_5:
        titre = p.get("title", "Produit")
        cat = p.get("category", "Général").capitalize()
        prix = f"{p.get('price', 0)} USD"
        note = p.get("rating", 4.5)
        stock = p.get("stock", 10)
        
        # Calcul algorithmique du score de viralité BOA
        score = min(100, int((note * 15) + (100 - stock) * 0.25))
        
        liste_finale.append({
            "id": f"ecom_{p.get('id')}",
            "title": titre,
            "category": cat,
            "price": prix,
            "viral_score": score,
            "image_url": p.get("thumbnail", ""),
            "sourcing_url": f"https://www.google.com/search?q={urllib.parse.quote(titre)}+sourcing+aliexpress",
            "market_context": f"Niche {cat}. Validé par l'algorithme de tendance BOA."
        })
        
    structure_json = {
        "last_updated": datetime.now().strftime("%H:%M"),
        "count": len(liste_finale),
        "items": liste_finale
    }

    # Sauvegarde directe dans le nouveau dossier data
    with open("data/ecom_products.json", "w", encoding="utf-8") as f:
        json.dump(structure_json, f, indent=4, ensure_ascii=False)
        
    print("Le fichier data/ecom_products.json a bien été mis à jour !")

except Exception as e:
    print(f"Erreur : {e}")
    exit(1)

