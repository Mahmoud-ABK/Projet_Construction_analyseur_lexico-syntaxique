from flask import Flask, render_template, request, jsonify
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from compilateur import analyseure_lexicale


app = Flask(__name__)

# Configuration pour le dossier d'uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Configuration pour le dossier qui contient les fichiers
Fichiers_FOLDER = "fichiers"
os.makedirs(Fichiers_FOLDER, exist_ok=True)
app.config["Fichiers_FOLDER"] = Fichiers_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    fichiers = os.listdir(app.config["Fichiers_FOLDER"])
    fichier_choisi = None
    contenu_fichier = None
    texte_genere = None
    
    if request.method == "POST":
        if "importer" in request.form:  # Importation d'un fichier
            fichier = request.files.get("fichier")
            if fichier and fichier.filename.endswith(".txt"):
                chemin_fichier = os.path.join(app.config["UPLOAD_FOLDER"], fichier.filename)
                fichier.save(chemin_fichier)
                fichier_choisi = fichier.filename
                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu_fichier = f.read()

        elif "ouvrir" in request.form:  # Sélection depuis la combobox
            fichier_choisi = request.form.get("fichier")
            if fichier_choisi:
                chemin_fichier = os.path.join(app.config["Fichiers_FOLDER"], fichier_choisi)
                with open(chemin_fichier, "r", encoding="utf-8") as f:
                    contenu_fichier = f.read()

    return render_template("index.html", fichiers=fichiers, fichier_choisi=fichier_choisi, contenu_fichier=contenu_fichier, texte_genere=texte_genere)

@app.route("/compiler", methods=["POST"])
def compiler():
    data = request.get_json()  
    texte = data.get("texte")  
    ################################
    #l'analyseur lexical
    tokens=analyseure_lexicale(texte)
    texte_genere = ''.join(''.join(map(str, tup)) for tup in tokens) 
    print(texte_genere)
    return jsonify({"texte_genere": texte_genere}) 

@app.route("/compilerSyntaxique", methods=["POST"])
def compilerSyntaquique():
    data = request.get_json() 
    texte = data.get("texte")  
    #ici on va appeler l'analyseur synatxique 
    texte_genere = "Arbre du fichier" 
    print(texte_genere)
    return jsonify({"texte_genere": texte_genere})  

@app.route("/compilerRecommandation", methods=["POST"])
def compilerRecommandation():
    data = request.get_json() 
    texte = data.get("texte")  
    #ici on va appeler le recommandateur
    texte_genere = "la recommandation du produit " 
    pourcentage_genere="75"
    print(texte_genere)
    return jsonify({"texte_genere": texte_genere,"pourcentage_genere": pourcentage_genere})  

if __name__ == '__main__':
    app.run(debug=True)



