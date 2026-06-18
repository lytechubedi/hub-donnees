async function chargerTendances() {
    try {
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        const donnees = await reponse.json();
        
        document.getElementById('flux-titre').textContent = donnees.titre_flux;
        document.getElementById('viral-statut').textContent = donnees.statut_reseau;
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour;
        
        // Gestion dynamique de l'image
        const imgElement = document.getElementById('produit-image');
        if (donnees.image_produit) {
            imgElement.src = donnees.image_produit;
            imgElement.style.display = 'block';
        }

        // Gestion du lien cliquable
        const lienElement = document.getElementById('produit-details');
        lienElement.textContent = donnees.valeur_crypto;
        lienElement.href = donnees.lien_sourcing;

    } catch (erreur) {
        console.error("Erreur lors de la synchronisation :", erreur);
    }
}

chargerTendances();

