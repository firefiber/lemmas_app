import json
import spacy
import nltk
from nltk.stem import WordNetLemmatizer

# Import the JSON file
with open("lemList.json", "r") as f:
  data = json.load(f)

# Load the Spanish language model
nlp = spacy.load('es_core_news_md')

# Create a WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()

# check if a key exists in a dictionary, with a given input
def check_key(dictionary, user_input):
    keys = list(dictionary.keys())
    if user_input in keys:
        return True
    return False

# Define a function to lemmatize a single word
def lemmatize_word(word, pos):
    pos = pos
    # Convert the part of speech to the corresponding WordNet tag
    # if pos == None:
    #     lemma = lemmatizer.lemmatize(word)
    # else:
    lemma = lemmatizer.lemmatize(word, pos=pos)
    # Return the lemma if found, or the original word if not
    return lemma


def lemmatize_words(word_list):
    lemmatized_words = []  
    for word in word_list:
        # Tokenize the word
        doc = nlp(word)
        for token in doc:
            # Get the lemma of the word and its part of speech
            lemma = token.text
            pos = token.pos_
            if pos in ['NOUN', 'PROPN', 'PRON']:  
                pos = 'n'
            elif pos in ['VERB']:  
                pos = 'v'
            elif pos in ['ADJ']: 
                pos = 'a'
            elif pos in ['ADV']:  
                pos = 'r'
            else:
                pos = '' 
            print(pos)
        # Lemmatize the word
        lemmatized_word = lemmatize_word(lemma, pos)
        # Append the lemmatized word to the list
        lemmatized_words.append(lemmatized_word)
    return lemmatized_words

# Create a new dict to store the items
freqList = {}

# Copy the items from the original array into lemList
for item in data["lemmas"]:
  freqList[item["lemma"]] = item["ID"]

# user input
input_text = input('Enter a word or sentence: ')

input_words = input_text.split()

lemmatized_words = lemmatize_words(input_words)
print(lemmatized_words)

for word in lemmatized_words:
    if word in freqList.keys():
        print(f"Word: {word} | Freq: {freqList[word]}")
