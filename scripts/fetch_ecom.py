import json
import os
import random
from datetime import datetime

# 1. Grand catalogue de produits e-commerce à forte tendance mondiale
POOL_PRODUITS = [
    {
        "title": "Mini Projecteur LED 4K Portable",
        "category": "High-Tech",
        "price": "39.99 USD",
        "market_context": "Explose sur TikTok. Idéal pour les soirées cinéma en plein air ou dans la chambre.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=mini+projector+4k"
    },
    {
        "title": "Brosse Nettoyante Visage Ultrasons",
        "category": "Beauté & Soins",
        "price": "14.50 USD",
        "market_context": "Forte demande en cosmétique. Produit à forte marge pour les boutiques de soins.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=ultrasonic+face+cleanser"
    },
    {
        "title": "Mousseur à Lait Électrique Sans Fil",
        "category": "Cuisine",
        "price": "6.20 USD",
        "market_context": "Tendance 'Home Cafe' très forte sur les réseaux. Petit, pas cher à expédier.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=electric+milk+frother"
    },
    {
        "title": "Sac à Doc Antivol avec Port de Charge USB",
        "category": "Mode & Voyage",
        "price": "18.90 USD",
        "market_context": "Le best-seller indémodable pour les étudiants et voyageurs. Très recherché.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=anti+theft+backpack+usb"
    },
    {
        "title": "Gourde Isotherme Intelligente avec Affichage LED",
        "category": "Sport & Fitness",
        "price": "8.50 USD",
        "market_context": "Affiche la température du liquide. Produit écologique très populaire.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=smart+led+vacuum+flask"
    },
    {
        "title": "Support Téléphone Magnétique pour Voiture (MagSafe)",
        "category": "Accessoires Auto",
        "price": "4.10 USD",
        "market_context": "Accessoire indispensable. Volume de vente extrêmement élevé sur les places de marché.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=magnetic+car+phone+holder"
    },
    {
        "title": "Masseur Oculaire Chauffant Bluetooth",
        "category": "Bien-être",
        "price": "22.00 USD",
        "market_context": "Aide à la relaxation et soulage la fatigue des écrans. Produit premium d'impulsion.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=heating+eye+massager"
    },
    {
        "title": "Mini Aspirateur Sans Fil pour Bureau et Voiture",
        "category": "Maison",
        "price": "11.30 USD",
        "market_context": "Gadget de nettoyage viral. Très fort taux de conversion en vidéo publicitaire.",
        "sourcing_url": "https://www.alibaba.com/trade/search?SearchText=mini+wireless+vacuum"
    }
]

def run_bot():
    print("Démarrage du scanner de tendances BOA...")
    
    # Sélectionner 5 produits au hasard dans notre grand catalogue
    produits_choisis = random.sample(POOL_PRODUITS, 5)
    
    items = []
    for p in produits_choisis:
        # Générer un score de viralité aléatoire mais élevé
        score_viral = random.randint(75, 98)
        
        items.append({
            "title": p["title"],
            "category": p["category"],
            "price": p["price"],
            "viral_score": score_viral,
            "market_context": p["market_context"],
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=150&auto=format&fit=crop", # Image propre
            "sourcing_url": p["sourcing_url"]
        })
    
    # Créer le dossier 'data' si jamais il n'existe pas
    os.makedirs("data", exist_ok=True)
    
    # Préparer le fichier de données final
    maintenant = datetime.now().strftime("%H:%M")
    data_finale = {
        "last_updated": maintenant,
        "items": items
    }
    
    # Sauvegarder dans le fichier JSON
    with open("data/ecom_products.json", "w", encoding="utf-8") as f:
        json.dump(data_finale, f, ensure_ascii=False, indent=4)
        
    print(f"Succès ! 5 nouveaux produits sauvegardés à {maintenant}.")

if __name__ == "__main__":
    run_bot()
