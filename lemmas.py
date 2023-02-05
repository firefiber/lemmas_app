# -*- coding: utf-8 -*-
import json
import spacy
import nltk
from nltk.stem import WordNetLemmatizer

# Import the JSON file
with open("lemList.json", "r", encoding="utf-8") as f:
  data = json.load(f)

# Load spaCy spanish lang model
nlp = spacy.load('es_core_news_md')

# init lemmatizer object
nltk_lemmatizer = WordNetLemmatizer()

# check if a key exists in a dictionary, with a given input
def check_key(dictionary, user_input):
    keys = list(dictionary.keys())
    if user_input in keys:
        return True
    return False

# NLTK DOES NOT WORK WELL ########## # takes an input, returns the lemma of that input
# def lemmatize(word):
#   lemmatizer = nltk.WordNetLemmatizer()
#   lemma = lemmatizer.lemmatize(word)
#   if lemma:
#     return lemma
#   else:
#     return word

# takes a single word, returns lemma if found. returns original if no lemma found (or if pronoun)
def lemmatizer(word):
  doc = nlp(word)
  for token in doc:
    lemma = token.lemma_
    if lemma != '-PRON-':
      return lemma
  return word


# Create a new dict to store the items
freqList = {}

# Copy the items from the original array into lemList
for item in data["lemmas"]:
  freqList[item["lemma"]] = item["ID"]

# Get user input
USR_input = input("Enter a word: ")
# split user input into an array
input_word_list = USR_input.split()
# array to store lemmatized words, returned from the lemmatize func
lemmatized_words = [lemmatizer(word) for word in input_word_list]

print(lemmatized_words)

# if check_key(lemList, USR_input):
#     print(f"Key: {USR_input} \n Value: {lemList[USR_input]}")
# else:
#     print("Key does not exist in dictionary")

# value = lemList.get(userInput, None)

# if value is not None:
#   print (lemList[userInput])
# else:
#   print("Key does not exist")

# # for key in lemList.keys():
# #     print(key)
# # # Loop over the keys and print them
# # for item in new_array:
# #   for key in item:
# #     print(key)

for word in lemmatized_words:
    if word in freqList.keys():
        print(f"Word: {word} | Freq: {freqList[word]}")



###TODO

# fix POS in JSON file
# pos in array
# try deepl api 
