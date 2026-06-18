async function chargerTendances() {
    try {
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        
        // Si le fichier n'existe pas encore sur le serveur
        if (!reponse.ok) {
            throw new Error("Fichier data.json introuvable (Erreur " + reponse.status + "). Lance le robot dans l'onglet Actions.");
        }
        
        const donnees = await reponse.json();
        
        document.getElementById('flux-titre').textContent = donnees.titre_flux || "Non défini";
        document.getElementById('viral-statut').textContent = donnees.statut_reseau || "Non défini";
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour || "--:--";
        
        // Gestion de l'image
        const imgElement = document.getElementById('produit-image');
        if (donnees.url_image) {
            imgElement.src = donnees.url_image;
            imgElement.style.display = 'block';
        }

        // Gestion du lien
        const lienElement = document.getElementById('produit-details');
        if (donnees.nom_produit) {
            lienElement.textContent = donnees.nom_produit;
        }
        if (donnees.url_produit) {
            lienElement.href = donnees.url_produit;
        }

    } catch (erreur) {
        console.error(erreur);
        // Affiche l'erreur directement à la place du texte pour le debug sur mobile
        document.getElementById('flux-titre').textContent = "⚠️ " + erreur.message;
        document.getElementById('flux-titre').style.color = "#ff6b6b";
    }
}

chargerTendances();
