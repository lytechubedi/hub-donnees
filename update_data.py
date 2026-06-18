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
    
    produits_tries = sorted(liste_produits, key=lambda x: (x.get("rating", 0), x.get("discountPercentage", 0)), reverse=True)
    top_produit = produits_tries[0]
    
    nom_produit = top_produit.get("title", "Produit inconnu")
    niche = top_produit.get("category", "Général").capitalize()
    prix = f"{top_produit.get('price', 0)} USD"
    note = top_produit.get("rating", 4.5)
    stock_restant = top_produit.get("stock", 10)
    
    image_url = top_produit.get("thumbnail", "")
    
    nom_encode = urllib.parse.quote(nom_produit)
    lien_sourcing = f"https://www.google.com/search?q={nom_encode}+sourcing+aliexpress"
    
    score_viralite = min(100, int((note * 15) + (100 - stock_restant) * 0.25))
    heure_actuelle = datetime.now().strftime("%H:%M")

    # Clés ultra-propres et explicites
    nouvelles_donnees = {
        "titre_flux": f"Radar de Tendances ({niche})",
        "statut_reseau": f"Viral à {score_viralite}%",
        "nom_produit": f"{nom_produit} — {prix}",
        "url_image": image_url,
        "url_produit": lien_sourcing,
        "derniere_mise_a_jour": heure_actuelle
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(nouvelles_donnees, f, indent=4, ensure_ascii=False)
        
    print("Fichier data.json synchronisé avec les nouvelles clés !")

except Exception as e:
    print(f"Erreur : {e}")
    exit(1)
