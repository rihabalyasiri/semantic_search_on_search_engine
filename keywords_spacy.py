
import json
import spacy

def extract_keywords(data, filename):
    # Load the German language model
    nlp = spacy.load("de_core_news_sm")
    for ad in data:
        # Process the text
        doc = nlp(ad["body_text"])

        # Extract keywords (nouns and proper nouns)
        keywords = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]
        ad["keywords"] = keywords

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)



with open("sample/ground_truth_adjusted.json", 'r') as file:
    german_data = json.load(file)

# Extract keywords
keywords = extract_keywords(german_data, "sample/ground_truth_adjusted.json")


