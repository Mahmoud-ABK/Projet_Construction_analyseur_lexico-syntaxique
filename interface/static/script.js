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
        // Display the generated text
        document.getElementById("generated-content_tokens").innerHTML = `
            <h2>Tokens:</h2>
            <p id="generated-text">${data.texte_genere}</p>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while compiling.");
    });
    document.getElementById("traitement_fichier").style.display = "none";
    document.getElementById("compile-section").style.display = "none";
    document.getElementById("boutonArbre").style.display = "flex";

});

// bouton generer arbre syntaxique
document.getElementById("arbreButton").addEventListener("click", function () {
    let tokens_affiche = document.getElementById("generated-text");
    // Check if there's any text to send
    if (!tokens_affiche) {
        alert("No text content found to compile!");
        return;
    }
    // Prepare the request
    fetch("/compilerSyntaxique", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ texte: tokens_affiche }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server Response:", data);
        // Display the generated text
        document.getElementById("generated-content_arbre").innerHTML = `
            <h2>Syntax tree:</h2>
            <p id="generated-arbre">${data.texte_genere}</p>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while compiling.");
    });
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
