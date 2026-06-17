// Ce script s'exécute dès que la page est chargée
document.addEventListener("DOMContentLoaded", () => {
    // On cherche l'élément qui a l'identifiant "data-box" pour modifier son texte
    const dataBox = document.getElementById("data-box");
    
    if (dataBox) {
        dataBox.innerText = "Moteur JavaScript actif. Prêt à recevoir le flux de données.";
        dataBox.style.color = "#4ade80"; // Change la couleur en vert pour confirmer le succès
    }
});

