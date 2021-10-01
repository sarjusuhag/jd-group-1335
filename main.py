from os import write
import nltk
import re

from nltk.util import tokenwrap

# download tokenization model
nltk.download("punkt")

# clean text
text = None
with open("frederickdouglasstext.txt", encoding="cp1252") as file:
    text = file.read()
    # ignores special characters such as �
    # lowercases all characters
    text = text.encode("ascii", "ignore").decode().lower()

tokens = nltk.word_tokenize(text)
print(tokens[:1000])

regexp = re.compile("[^A-Za-z0-9-]")

with open("tokens.txt", "w") as outfile:
    outfile.write("\n".join([token for token in tokens if not regexp.search(token)]))

# how to deal with special characters? (ÊÊÊÊÊÊÊÊ)
# then do a set intersection of text and known words w/ words that are lowercased
