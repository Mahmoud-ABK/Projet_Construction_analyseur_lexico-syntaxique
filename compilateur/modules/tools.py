import re
import spacy
import csv

# Load SpaCy French model
nlp = spacy.load("fr_core_news_sm")


# Load product names from the CSV file
def load_product_names(csv_file):
    product_names = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_names.append(row['product_name'].lower())  # Normalize to lowercase for matching
    return product_names

# Create regex pattern to match all product names
def create_product_regex(product_names):
    escaped_names = [re.escape(name) for name in product_names]
    return r'\b(?:' + '|'.join(escaped_names) + r')\b'

# Function to match product names in the text
def match_product_name(texte, index, product_regex):
    match = re.match(product_regex, texte[index:].lower())
    if match:
        return match.group(0), len(match.group(0))
    return None, 0

# Function to match symbols (e.g., punctuation)
def match_symbol(texte, index):
    match = re.match(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_`{|}~]', texte[index:])
    if match:
        return match.group(0), len(match.group(0))
    return None, 0

# Function to match words (MOT)
def match_word(texte, index):
    match = re.match(r"[A-Za-zÀ-ÿ']+", texte[index:])
    if match:
        return match.group(0), len(match.group(0))
    return None, 0


# Function to match numbers (integers, decimals)
def match_number(texte, index):
    # Regular expression to match numbers, including decimals
    number_pattern = r'\b\d+(\.\d+)?\b'
    match = re.match(number_pattern, texte[index:])
    if match:
        return match.group(0), len(match.group(0))  # Return matched number and its length
    return None, 0  # No match, return None and 0 length
# Function to classify words using SpaCy NLP (e.g., NOUN, ADJ, NUM, VERB) and additional NUMBER and UNIT
# Function to classify words with unit recognition
def classify_word(word):
    categories = []

    # Define the regex pattern for units
    unit_pattern = r'\b(cm|kg|h|minutes|hours|m|GB|inches|Go|mAh|pouces)'

    # Check if the word matches a unit
    if re.match(unit_pattern, word):
        categories.append(("UNIT", word))
    else:
        # Check with SpaCy NLP model for other categories
        doc = nlp(word)
        for token in doc:
            if token.pos_ == "NOUN":
                categories.append(("FEATURE", token.text))
            elif token.pos_ == "ADJ":
                categories.append(("ADJ", token.text))
            elif token.pos_ == "NUM":
                categories.append(("NUMBER", token.text))
            elif token.pos_ == "VERB":
                categories.append(("VERB", token.text))
            elif token.pos_ == "ADV":
                categories.append(("ADV", token.text))
            elif token.pos_ == "DET":
                categories.append(("DET", token.text))
            else:
                categories.append(("MOT", token.text))

    return categories