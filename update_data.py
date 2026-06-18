import json
import urllib.request
from datetime import datetime

# API publique de produits mondiaux (Sans clé nécessaire)
url = "https://dummyjson.com/products?limit=30"

try:
    # Connexion sécurisée à l'API de sourcing
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        source_brute = response.read().decode()
        
    donnees_api = json.loads(source_brute)
    liste_produits = donnees_api.get("products", [])
    
    # ALGORITHME SENIOR : Tri par popularité (note) et taux de promotion
    # Identifie le produit le plus rentable et attractif du moment
    produits_tries = sorted(liste_produits, key=lambda x: (x.get("rating", 0), x.get("discountPercentage", 0)), reverse=True)
    top_produit = produits_tries[0]
    
    # Extraction des indicateurs clés du produit gagnant
    nom_produit = top_produit.get("title", "Produit inconnu")
    niche = top_produit.get("category", "Général").capitalize()
    prix = f"{top_produit.get('price', 0)} USD"
    note = top_produit.get("rating", 4.5)
    stock_restant = top_produit.get("stock", 10)
    
    # Calcul dynamique du Score de Viralité TikTok/Shorts (sur 100)
    score_viralite = min(100, int((note * 15) + (100 - stock_restant) * 0.25))
    
    heure_actuelle = datetime.now().strftime("%H:%M")

    # Reconstruction du JSON (Adapté temporairement aux clés existantes pour éviter les bugs)
    nouvelles_donnees = {
        "titre_flux": f"Radar de Tendances ({niche})",
        "statut_reseau": f"Viral à {score_viralite}%",
        "valeur_crypto": f"{nom_produit} — {prix}",
        "derniere_mise_a_jour": heure_actuelle
