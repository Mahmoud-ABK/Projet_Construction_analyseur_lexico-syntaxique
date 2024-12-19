from analyse_lexicale import analyseure_lexicale
token_types = [
    "PRODUCT",
    "FEATURE",
    "NUMBER",
    "UNIT",
    "ADJ",
    "VERB",
    "MOT"
]
def parseur(tokens, grammaire=None):
    """
    Analyse une liste de tokens et construit un arbre syntaxique tout en le validant selon une grammaire.

    Arguments:
        tokens (list): Une liste de tuples représentant les tokens (type_de_token, valeur).
        grammaire (dict, optionnel): Règles de grammaire spécifiant les occurrences minimales et maximales pour chaque type de token.

    Retourne:
        dict: Un arbre syntaxique qui associe les types de tokens à leurs listes de valeurs correspondantes.
        str: Un message décrivant le résultat de la validation.
        bool: Résultat de la validation (True si les tokens respectent la grammaire, False sinon).
    """
    # Définir la grammaire par défaut
    grammaire = grammaire or {
        "PRODUCT": {"min": 1, "max": 1},
        "FEATURE": {"min": 2, "max": None},
        "ADJ": {"min": 2, "max": None},
    }

    # Initialiser les compteurs et l'arbre syntaxique
    compte_tokens = {type_token: 0 for type_token in token_types}
    arbre_syntaxique = {type_token: [] for type_token in token_types}

    # Classer les tokens dans l'arbre syntaxique
    for type_token, valeur in tokens:
        if type_token in arbre_syntaxique:
            if valeur not in arbre_syntaxique[type_token]:
                arbre_syntaxique[type_token].append(valeur)
                compte_tokens[type_token] += 1

    # Valider les comptes de tokens par rapport aux règles de la grammaire
    for type_token, regles in grammaire.items():
        compte = compte_tokens.get(type_token, 0)
        min_compte = regles.get("min", 0)
        max_compte = regles.get("max", None)
        if compte_tokens['PRODUCT']!=1:
            return {}, f"Erreur : L'article doit contenir un est un seul produit . Trouvé : {compte_tokens['PRODUCT']}.", False
        if compte < min_compte:
            return {}, f"Erreur : L'article doit contenir au moins {min_compte} token(s) de type {type_token}. Trouvé : {compte}.", False
        if max_compte is not None and compte > max_compte:
            return {}, f"Erreur : L'article doit contenir au maximum {max_compte} token(s) de type {type_token}. Trouvé : {compte}.", False

    # Si tout est valide, retourner l'arbre syntaxique
    return arbre_syntaxique, "L'article est valide.", True

"""
test="Le Samsung Galaxy S23 Samsung Galaxy S23 Apple iPhone 15 offre un ensemble convaincant pour ceux qui recherchent une Hz expérience To smartphone Go haut de gamme dans un format compact. Propulsé par le dernier processeur Snapdragon 8 Gen 2, il offre des performances exceptionnelles pour les tâches exigeantes. Son écran Dynamic AMOLED 2X offre des visuels époustouflants avec des noirs profonds, des couleurs vibrantes et un taux de rafraîchissement fluide de 120 Hz. Le système de caméra polyvalent capture des photos et des vidéos détaillées, même dans des conditions de faible éclairage. La construction robuste du téléphone avec la protection Gorilla Glass Victus 2 garantit sa durabilité. Bien que l'autonomie de la batterie du S23 soit impressionnante, elle pourrait être meilleure, surtout pour les utilisateurs intensifs. De plus, les options de stockage limitées et le prix élevé peuvent être des inconvénients pour certains. Dans l'ensemble, le S23 est un smartphone fantastique qui offre un excellent équilibre entre performances, fonctionnalités et design."
tokens=analyseure_lexicale(test)
for token in tokens:
    a,b=token
    print(a,' ',b)
arbre,message,correct=parseur(tokens)
print("correct",correct)
print('message',message)
print('arbre ----------------------------')
for key, valeur in arbre.items():
    print(key,' ',valeur)
"""