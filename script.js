async function chargerTendances() {
    try {
        // Le paramètre '?t=' brise le cache des téléphones pour afficher le produit instantanément
        const reponse = await fetch('data.json?t=' + new Date().getTime());
        const donnees = await reponse.json();
        
        document.getElementById('flux-titre').textContent = donnees.titre_flux;
        document.getElementById('viral-statut').textContent = donnees.statut_reseau;
        document.getElementById('produit-details').textContent = donnees.valeur_crypto;
        document.getElementById('maj-heure').textContent = donnees.derniere_mise_a_jour;
    } catch (erreur) {
        console.error("Erreur lors de la synchronisation du dashboard :", erreur);
    }
}

// Lancement automatique au chargement de la page
chargerTendances();

