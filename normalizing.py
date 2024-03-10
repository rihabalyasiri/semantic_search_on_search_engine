import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from num2words import num2words
import nltk

def normalizing(sentence):
    sentence = convert_lower_case(sentence)
    sentence = remove_punctuation(sentence)
    sentence = remove_apostrophe(sentence)
    sentence = remove_stop_words(sentence)
    sentence = convert_numbers(sentence)
    sentence = stemming(sentence)
    sentence = remove_punctuation(sentence)
    sentence = convert_numbers(sentence)
    sentence = stemming(sentence)
    sentence = remove_punctuation(sentence)
    sentence = remove_stop_words(sentence)

    return sentence

def convert_lower_case(sentence):
    return np.char.lower(sentence)

def remove_stop_words(sentence):
    stop_words = stopwords.words("german")
    words = word_tokenize(str(sentence))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text

def remove_punctuation(sentence):
   symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
   for i in range(len(symbols)):
       sentence = np.char.replace(sentence, symbols[i], ' ')
       sentence = np.char.replace(sentence, "  ", " ")
       sentence = np.char.replace(sentence, ',', '')
   return sentence


def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


def stemming(sentence):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(sentence))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text


def convert_numbers(sentence):
    
    tokens = word_tokenize(str(sentence))
    new_text = ""
    for w in tokens:
        try:
            # Convert to number word in German
            w = num2words(int(w), lang='de')
        except ValueError:
            # If conversion fails, keep the word as it is
            pass
        new_text += " " + w.replace("-", " ")
    # Strip leading/trailing spaces and return
    return new_text.strip()

