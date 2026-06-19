document.addEventListener("DOMContentLoaded", () => {
    const conteneur = document.body;
    
    // 1. Création d'une zone propre pour accueillir nos cartes de produits
    const zoneCatalogue = document.createElement("div");
    zoneCatalogue.id = "catalogue-booster";
    zoneCatalogue.style.cssText = "display: flex; flex-direction: column; gap: 20px; padding: 10px; max-width: 500px; margin: 0 auto;";
    
    // On cherche l'ancien bloc de vérification pour insérer notre catalogue juste au-dessus
    const footer = document.querySelector("div:last-of-type");
    if (footer) {
        footer.parentNode.insertBefore(zoneCatalogue, footer);
    } else {
        conteneur.appendChild(zoneCatalogue);
    }

    // 2. Chargement des données fraîches du robot
    // Le "?t=" force le téléphone à charger les vrais nouveaux produits sans rester bloqué sur une ancienne version
    fetch("data/ecom_products.json?t=" + new Date().getTime())
        .then(reponse => reponse.json())
        .then(data => {
            // On vide la zone avant d'afficher
            zoneCatalogue.innerHTML = "";
            
            // 3. Boucle pour afficher chaque produit un par un
            data.items.forEach(produit => {
                const carte = document.createElement("div");
                carte.style.cssText = "background: #1a233a; border: 1px solid #2c3b59; border-radius: 12px; padding: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);";
                
                carte.innerHTML = `
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.85em;">
                        <span style="background: #2563eb; color: white; padding: 2px 8px; border-radius: 20px;">${produit.category}</span>
                        <span style="color: #34d399; font-weight: bold;">🔥 Viral : ${produit.viral_score}%</span>
                    </div>
                    <img src="${produit.image_url}" alt="${produit.title}" style="width: 80px; height: 80px; object-fit: contain; border-radius: 8px; background: #0f172a; padding: 5px; margin: 10px 0;">
                    <h3 style="margin: 5px 0; color: #fff; font-size: 1.1em;">${produit.title}</h3>
                    <p style="color: #cbd5e1; margin: 5px 0; font-size: 0.95em;">Prix indicatif : <span style="color: #38bdf8; font-weight: bold;">${produit.price}</span></p>
                    <p style="color: #94a3b8; font-size: 0.8em; font-style: italic; margin: 10px 0;">${produit.market_context}</p>
                    <a href="${produit.sourcing_url}" target="_blank" style="display: inline-block; background: #10b981; color: white; text-decoration: none; padding: 8px 15px; border-radius: 6px; font-size: 0.9em; font-weight: bold; margin-top: 5px;">Rechercher le fournisseur 🔍</a>
                `;
                zoneCatalogue.appendChild(carte);
            });
            
            // Mise à jour de l'heure de vérification en bas du site
            const verifBox = document.querySelector("div:last-of-type p") || footer;
            if (verifBox) {
                verifBox.innerHTML = `Mise à jour BOA à : ${data.last_updated}`;
            }
        })
        .catch(erreur => {
            console.error("Erreur de liaison :", erreur);
            zoneCatalogue.innerHTML = "<p style='color: #ef4444; text-align:center;'>Mise à jour du flux en cours...</p>";
        });
});
