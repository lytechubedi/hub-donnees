import json
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

def run_bot():
    print("Connexion en direct au flux officiel Google Trends France...")
    # Flux RSS public de Google Trends pour la France (évite les blocages de serveurs)
    url = "https://trends.google.com/trending/rss?geo=FR"
    
    try:
        # Configuration de la requête pour simuler un navigateur propre
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        # Lecture du contenu XML envoyé par Google
        root = ET.fromstring(xml_data)
        items = []
        
        # Les namespaces spécifiques utilisés par Google dans son flux XML
        namespaces = {
            'ht': 'http://www.google.com/trends/category/trendingsearches'
        }
        
        count = 0
        for item in root.findall('.//item'):
            if count >= 5:
                break
                
            # Extraire le mot-clé ou sujet réel qui explose sur Google
            title = item.find('title').text
            
            # Extraire le volume réel de recherches (ex: 50 000+ recherches)
            traffic_elem = item.find('ht:approx_traffic', namespaces)
            traffic = traffic_elem.text if traffic_elem is not None else "Forte hausse"
            
            # Extraire l'image d'actualité liée par Google
            picture_elem = item.find('ht:picture', namespaces)
            image_url = picture_elem.text if picture_elem is not None else "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=150"
            
            # Encoder le mot-clé pour créer un lien de sourcing/analyse propre vers Google Trends
            encoded_query = urllib.parse.quote(title)
            sourcing_url = f"https://trends.google.com/trends/explore?q={encoded_query}&geo=FR"
            
            # Construire la fiche dynamique basée sur la vraie tendance du jour
            items.append({
                "title": f"Tendance : {title}",
                "category": "Google Trends Live",
                "price": f"{traffic} requêtes",
                "viral_score": 99 - count, # Score basé sur la position dans le top France
                "market_context": f"Sujet actuellement dans le Top 5 des recherches Google en France. Intérêt du public maximal à exploiter immédiatement.",
                "image_url": image_url,
                "sourcing_url": sourcing_url
            })
            count += 1
            
        # Création du dossier de stockage si nécessaire
        os.makedirs("data", exist_ok=True)
        
        # Enregistrement des données avec l'heure
        maintenant = datetime.now().strftime("%H:%M")
        data_finale = {
            "last_updated": maintenant,
            "items": items
        }
        
        with open("data/ecom_products.json", "w", encoding="utf-8") as f:
            json.dump(data_finale, f, ensure_ascii=False, indent=4)
            
        print(f"Succès total ! 5 tendances réelles extraites de Google France à {maintenant}.")
        
    except Exception as e:
        print(f"Erreur technique lors de la liaison Google Trends : {e}")
        raise e

if __name__ == "__main__":
    run_bot()
