import json
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

def run_bot():
    print("Connexion en direct au flux officiel Google Trends France...")
    url = "https://trends.google.com/trending/rss?geo=FR"
    
    # Catalogue de secours : 5 superbes visuels e-commerce différents pour éviter les doublons
    FALLBACK_IMAGES = [
        "https://images.unsplash.com/photo-1526738549149-8e07eca6c147?w=400&auto=format&fit=crop&q=80", # Gadget Tech Moderne
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&auto=format&fit=crop&q=80", # Sneaker Rouge Virale
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&auto=format&fit=crop&q=80", # Produit Minimaliste Blanc
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&auto=format&fit=crop&q=80", # Casque Audio Premium
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&auto=format&fit=crop&q=80"  # Art Abstrait Tendance 3D
    ]
    
    try:
        # Simulation d'un navigateur classique
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        items = []
        
        count = 0
        for item in root.findall('.//item'):
            if count >= 5:
                break
                
            title = item.find('title').text
            
            # Initialisation des variables
            traffic = "Forte hausse"
            google_image = None
            
            # Extraction intelligente sans se faire bloquer par les namespaces
            for child in item:
                if child.tag.endswith('approx_traffic'):
                    traffic = child.text if child.text else "Forte hausse"
                elif child.tag.endswith('picture'):
                    google_image = child.text
            
            # Sélection de l'image : celle de Google si elle existe, sinon une image unique du catalogue
            if google_image and google_image.startswith("http"):
                image_url = google_image
            else:
                image_url = FALLBACK_IMAGES[count % len(FALLBACK_IMAGES)]
            
            # Encodage propre du lien de sourcing Google Trends
            encoded_query = urllib.parse.quote(title)
            sourcing_url = f"https://trends.google.com/trends/explore?q={encoded_query}&geo=FR"
            
            # Structuration de la fiche produit / tendance
            items.append({
                "title": f"Tendance : {title}",
                "category": "Google Trends Live",
                "price": f"{traffic} recherches",
                "viral_score": 99 - count, # Classement dynamique décroissant
                "market_context": f"Sujet chaud actuellement dans le Top 5 Google France. Volume d'intérêt maximal détecté en temps réel.",
                "image_url": image_url,
                "sourcing_url": sourcing_url
            })
            count += 1
            
        # Sauvegarde propre dans le dossier data
        os.makedirs("data", exist_ok=True)
        maintenant = datetime.now().strftime("%H:%M")
        data_finale = {
            "last_updated": maintenant,
            "items": items
        }
        
        with open("data/ecom_products.json", "w", encoding="utf-8") as f:
            json.dump(data_finale, f, ensure_ascii=False, indent=4)
            
        print(f"Succès ! Les 5 tendances ont été diversifiées visuellement à {maintenant}.")
        
    except Exception as e:
        print(f"Erreur technique : {e}")
        raise e

if __name__ == "__main__":
    run_bot()
