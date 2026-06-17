document.addEventListener("DOMContentLoaded", () => {
    const dataBox = document.getElementById("data-box");
    
    // Récupération dynamique du fichier JSON
    fetch("data.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Impossible de lire le fichier de données.");
            }
            return response.json();
        })
        .then(data => {
            // Injection des données structurées dans le paragraphe HTML
            dataBox.innerHTML = `
                Flux : ${data.titre_flux}<br>
                Statut : <span style="color: #4ade80;">${data.statut_reseau}</span><br>
                Crypto : <span style="color: #38bdf8;">${data.valeur_crypto}</span><br>
                Mise à jour : ${data.derniere_mise_a_jour}
            `;
        })
        .catch(error => {
            dataBox.innerText = "Erreur critique de synchronisation des données.";
            dataBox.style.color = "#ef4444"; // Rouge en cas de panne
        });
});
