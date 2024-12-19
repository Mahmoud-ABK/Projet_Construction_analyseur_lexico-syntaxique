document.addEventListener("DOMContentLoaded", () => {
    const dropZone = document.getElementById("drop-zone");
    const fileInput = document.getElementById("fileInput");
    //const chooseFile = document.getElementById("chooseFile");
    const uploadForm = document.getElementById("uploadForm");

    // Clique pour choisir un fichier
    /*
    chooseFile.addEventListener("click", () => {
        fileInput.click(); // Ouvre la boîte de dialogue de fichier
    });*/


    // Gestion des événements de drag-and-drop
    dropZone.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", () => {
        dropZone.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropZone.classList.remove("dragover");

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            const dataTransfer = new DataTransfer();
            for (let i = 0; i < files.length; i++) {
                dataTransfer.items.add(files[i]);
            }
            fileInput.files = dataTransfer.files; // Associe les fichiers au champ fileInput
        }
    });
});

// bouton Compiler
document.getElementById("compileButton").addEventListener("click", function () {
    // Extract text content from the file display
    let textContent = document.querySelector("pre").innerText;
    // Check if there's any text to send
    if (!textContent) {
        alert("No text content found to compile!");
        return;
    }
    // Prepare the request
    fetch("/compiler", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ texte: textContent }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server Response:", data);
    
        // Récupérer la liste de tokens
        const tokens = data.tokens;
    
        // Construire un contenu HTML à partir de la liste
        let tokenHTML = "<h2>Tokens:</h2><ul>"; // Utilisation d'une liste non ordonnée (ul)
        tokens.forEach(tuple => {
            const tupleContent = tuple.map(item => `<span>${item}</span>`).join(", ");
            tokenHTML += `<li>&lt;${tupleContent}&gt;</li>`;
    });
        tokenHTML += "</ul>";
    
        // Ajouter le contenu généré au conteneur HTML
        document.getElementById("generated-content_tokens").innerHTML = tokenHTML;
    })
    .catch(error => console.error("Erreur:", error));
        
    document.getElementById("traitement_fichier").style.display = "none";
    document.getElementById("compile-section").style.display = "none";
    document.getElementById("boutonArbre").style.display = "flex";

});

// bouton generer arbre syntaxique

document.getElementById("arbreButton").addEventListener("click", function () {
    // Envoyer la requête au serveur
    fetch("/compilerSyntaxique", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
    })
        .then(response => response.json())
        .then(data => {
            console.log("Server Response:", data);

            // Extraire les données de l'arbre et validation 
            const arbre = data.arbre;
            const texteValidation = data.validation;
            const texteMessage = data.message;
            let treeHTML='';
            if(texteValidation){
                treeHTML += `<h2>${texteMessage}</h2>`;
                // Extraire le nom du produit
                const nomProduit = arbre["Nom produit"];
                delete arbre["Nom produit"]; // Supprimer pour ne pas le traiter comme un nœud

                // Fonction récursive pour générer le HTML de l'arbre avec un style |__ pour les nœuds
                function renderTree(node, tree, prefix = "") {
                    // Vérifier si le nœud a des enfants (feuilles)
                    if (Array.isArray(tree[node])) {
                        // Si c'est un nœud avec des feuilles, afficher les feuilles
                        let childrenHTML = tree[node].map(leaf => {
                            return `<li>${prefix}|__ <strong>${leaf}</strong></li>`;
                        }).join("");
                        return `<li>${prefix}|__ ${node}<ul>${childrenHTML}</ul></li>`;
                    } else {
                        // Si ce n'est pas un tableau, c'est une feuille
                        return `<li>${prefix}|__ ${node}: <strong>${tree[node]}</strong></li>`;
                    }
                }

                // Construire l'arbre complet en HTML
                treeHTML += `<h2>${nomProduit}</h2>`;
                treeHTML += `<ul>`;
                for (let node in arbre) {
                    const nodeHTML = renderTree(node, arbre);
                    if (nodeHTML) {  // Ajouter uniquement si le nœud existe
                        treeHTML += nodeHTML;
                    }
                }
                treeHTML += `</ul>`;

                // Afficher l'arbre généré dans la page
                document.getElementById("generated-content_arbre").innerHTML = treeHTML;
                }
            else{
                treeHTML += `<h2>${texteMessage}</h2>`;
                // Afficher l'arbre généré dans la page
                document.getElementById("generated-content_arbre").innerHTML = treeHTML;
            }
            
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while compiling.");
        });

    // Cacher les boutons et autres contenus inutiles
    document.getElementById("generated-content_tokens").style.display = "none";
    document.getElementById("boutonArbre").style.display = "none";
    document.getElementById("boutonRecommandation").style.display = "flex";
});


//bouton de recomandation
document.getElementById("recommandationButton").addEventListener("click", function () {
   //je vais laisser pre text car dans api gimini nou allons faire entre le texte et pas l'arbre ou les tokens
   let textContent = document.querySelector("pre").innerText;
    // Check if there's any text to send
    if (!textContent) {
        alert("No text content found to compile!");
        return;
    }
    // Prepare the request
    fetch("/compilerRecommandation", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ texte: textContent }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server Response:", data);
        // Display the generated text
        document.getElementById("generated-content_recommandation").innerHTML = `
            <h2>Recommendation:</h2>
            <p>${data.texte_genere}</p>
            <div class="percentage-container">
                <div class="circle">
                ${data.pourcentage_genere}
                </div>
            </div>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while compiling.");
    });
    document.getElementById("generated-content_arbre").style.display = "none";
    document.getElementById("boutonRecommandation").style.display = "none";
    
});
