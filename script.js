async function chargerTendances() {
    try {
        // Le "?t=" force ton téléphone à télécharger la version la plus récente sans cache
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        const donnees = await reponse.json();
        
        // 1. Affichage de l'heure
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour || "--:--";
        
        const conteneur = document.getElementById('conteneur-produits');
        
        // 2. Vérification du format du fichier data.json
        if (!donnees.produits || !Array.isArray(donnees.produits)) {
            // Si le robot Python n'a pas encore tourné, on affiche ce message d'attente pro
            conteneur.innerHTML = `
                <div class="card" style="text-align: center;">
                    <p style="color: #64ffda; font-weight: bold;">🔄 Transition vers le Top 5 en cours...</p>
                    <p style="font-size: 0.9em; color: #8892b0;">Le fichier de données doit être régénéré. Active le robot dans l'onglet Actions de GitHub.</p>
                </div>
            `;
            return;
        }
        
        // 3. Si le Top 5 est prêt, on nettoie et on injecte les 5 cartes
        conteneur.innerHTML = ""; 
        
        donnees.produits.forEach(produit => {
            const carte = document.createElement('div');
            carte.className = 'card';
            carte.style.marginBottom = '20px'; // Espace élégant entre les cartes
            
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
        console.error("Erreur :", erreur);
        document.getElementById('conteneur-produits').innerHTML = `
            <div class="card" style="text-align: center; border: 1px solid #ff6b6b;">
                <p style="color: #ff6b6b; font-weight: bold;">⚠️ Erreur de chargement</p>
                <p style="font-size: 0.85em; color: #8892b0;">Impossible de lire le catalogue des tendances.</p>
            </div>
        `;
    }
}

chargerTendances();
