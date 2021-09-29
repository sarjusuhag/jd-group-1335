import nltk

# download tokenization model
nltk.download("punkt")

# read text
text = None
with open("text.txt", encoding="cp1252") as file:
    # just read 100 bytes for now
    text = file.read(10000)

tokens = nltk.word_tokenize(text)
print(tokens)

# how to deal with special characters? (ÊÊÊÊÊÊÊÊ)
# then do a set intersection of text and known words w/ words that are lowercased
