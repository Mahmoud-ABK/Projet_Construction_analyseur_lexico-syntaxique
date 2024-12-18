from modules.tools import load_product_names, create_product_regex, match_product_name, match_symbol, match_word, match_number, classify_word

def analyseure_lexicale(texte):
    # Load product names from the CSV file
    csv_file="compilateur/csv/products.csv"
    product_names = load_product_names(csv_file)
    product_regex = create_product_regex(product_names)
    tokens = []

    index = 0
    while index < len(texte):
        # Match product name
        product, length = match_product_name(texte, index, product_regex)
        if product:
            tokens.append(("PRODUCT", product))
            index += length
            continue

        # Match symbol
        symbol, length = match_symbol(texte, index)
        if symbol:
            tokens.append(("SYMBOLE", symbol))
            index += length
            continue
        # Match number (before matching words)
        number, length = match_number(texte, index)
        if number:
            tokens.append(("NUMBER", number))
            index += length
            continue

        # Match word
        word, length = match_word(texte, index)
        if word:
            word_tokens = classify_word(word)
            tokens.extend(word_tokens)
            index += length
            continue

        # Skip unrecognized characters (whitespace or others)
        index += 1

    return tokens

# Example usage with a product article and product list from CSV
#article = 
"""
Le Samsung Galaxy S23 est un smartphone haut de gamme avec un écran de 6.1 pouces et une batterie de 4000mAh.
Il est disponible en version 128Go et 256Go.
"""

# Analyze the article and print the results
"""tokens = analyse_lexicale(article)

for token in tokens:
    print(token)"""
