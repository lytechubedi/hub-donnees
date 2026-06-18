async function chargerTendances() {
    try {
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        const donnees = await reponse.json();
        
        document.getElementById('flux-titre').textContent = donnees.titre_flux;
        document.getElementById('viral-statut').textContent = donnees.statut_reseau;
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour;
        
        // Affichage dynamique de la photo du produit
        const imgElement = document.getElementById('produit-image');
        if (donnees.url_image) {
            imgElement.src = donnees.url_image;
            imgElement.style.display = 'block';
        }

        // Configuration du lien hypertexte de sourcing
        const lienElement = document.getElementById('produit-details');
        if (donnees.nom_produit) {
            lienElement.textContent = donnees.nom_produit;
        }
        if (donnees.url_produit) {
            lienElement.href = donnees.url_produit;
        }

    } catch (erreur) {
        console.error("Erreur de synchronisation du dashboard :", erreur);
    }
}

chargerTendances();
