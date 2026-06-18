async function chargerTendances() {
    try {
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        const donnees = await reponse.json();
        
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour;
        
        const conteneur = document.getElementById('conteneur-produits');
        conteneur.innerHTML = ""; // On nettoie le texte de chargement
        
        // BOUCLE DYNAMIQUE : Génère une carte complète pour chaque produit du Top 5
        donnees.produits.forEach(produit => {
            const carte = document.createElement('div');
            carte.className = 'card';
            carte.style.marginBottom = '25px'; // Ajoute un espace élégant entre chaque produit
            
            carte.innerHTML = `
                <p><strong>Analyse :</strong> <span>Radar de Tendances (${produit.niche})</span></p>
                <p><strong>Potentiel TikTok/Shorts :</strong> <span>${produit.score}</span></p>
                
                <div style="text-align: center; margin: 15px 0;">
                    <img src="${produit.url_image}" alt="Aperçu" style="max-width: 130px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); margin: 0 auto; display: block;">
                </div>

                <p><strong>Produit Gagnant :</strong> <a href="${produit.url_produit}" target="_blank" style="color: #64ffda; text-decoration: underline; font-weight: bold;">${produit.nom} — ${produit.prix}</a></p>
            `;
            
            conteneur.appendChild(carte);
        });

    } catch (erreur) {
        console.error("Erreur lors de la génération de la liste :", erreur);
        document.getElementById('conteneur-produits').innerHTML = `<p style="color: #ff6b6b; text-align: center;">⚠️ Erreur de synchronisation du catalogue.</p>`;
    }
}

chargerTendances();
