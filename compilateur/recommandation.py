import google.generativeai as genai
import json
import re


# Configuration de l'API
genai.configure(api_key="AIzaSyBcsdy0ZNm4yH-6EjRYJpiwax7niGZXAt4")

# Créer le modèle
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,  # Valeur ajustée pour être valide
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def analyser_produit(texte):

    chat_session = model.start_chat(history=[])

    # Construire la requête
    prompt = f"""
    Analyse les informations suivantes :
    1. Extrait le **nom du produit** si possible, sinon propose un nom basé sur le contexte.
    2. Fournis une **description concise** basée sur la phrase d'entrée.
    3. Donne un **pourcentage de recommandation** (entre 0% et 100%) basé sur l'avis ou les sentiments exprimés.
    4. La structure à retourner est : dict (Nom : nom de produit, Description : description de produit, pourcentage : pourcentage de recommandation)
    Phrase d'entrée : '{texte}' 
    """

    try:
        # Envoi de la requête à l'API
        response = chat_session.send_message(prompt)

        # Extraire le résultat brut de l'API
        result = response.text.strip()

        # Retourner la réponse brute
        return result
    
    except genai.types.generation_types.StopCandidateException as e:
        print("La phrase a été bloquée par les filtres de sécurité de l'API.")
        print(f"Raison : {e}")
        return None

# Exemple d'utilisation
texte = "Le casque audio XYZ offre une qualité sonore exceptionnelle avec des basses profondes et une réduction de bruit active. Il est très confortable à porter pendant des heures."
texte1 = "Le laptop DEF a un design élégant et un écran haute résolution. Cependant, la performance du processeur est décevante, et la batterie ne dure pas aussi longtemps que prévu. C'est un bon choix pour des tâches légères, mais pas pour des applications intensives."
texte2 = "Le casque audio ABC offre une qualité sonore exceptionnelle avec des basses profondes et une réduction de bruit active. Il est très confortable à porter pendant des heures et la batterie dure toute la journée."



resultat = analyser_produit(texte)
resultat1 = analyser_produit(texte1)
resultat2 = analyser_produit(texte2)




def convertir(result):

    # Initialiser les valeurs par défaut
    nom_produit = "Inconnu"
    description = "Aucune description"
    pourcentage_recommandation = "0"

    # Recherche du nom du produit
    nom_index = result.find('"Nom":')
    if nom_index != -1:
        start = result.find('"', nom_index + 6) + 1
        end = result.find('"', start)
        nom_produit = result[start:end]

    # Recherche de la description
    description_index = result.find('"Description":')
    if description_index != -1:
        start = result.find('"', description_index + 14) + 1
        end = result.find('"', start)
        description = result[start:end]

    # Recherche du pourcentage de recommandation
    pourcentage_index = result.find('"pourcentage":')
    if pourcentage_index != -1:
        start = result.find(":", pourcentage_index) + 1
        end = result.find(",", start)
        if end == -1:  # Si c'est le dernier élément, on prend jusqu'à la fin
            end = result.find("}", start)
        pourcentage_recommandation = result[start:end].strip()

    # Retourner le dictionnaire avec les informations extraites
    return {
        "Nom": nom_produit,
        "Description": description,
        "pourcentage": pourcentage_recommandation
    }
def rec(text):
    t=analyser_produit(text)
    return convertir(t)
#print(rec(texte))




