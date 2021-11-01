from os import write
import nltk
import re

from nltk.util import tokenwrap


def tokenize():
    # download tokenization model
    nltk.download("punkt")

    # clean text
    text = None
    with open("./assets/frederickdouglasstext.txt", encoding="cp1252") as file:
        text = file.read()
        # ignores special characters such as �
        # lowercases all characters
        text = text.encode("ascii", "ignore").decode().lower()

    tokens = nltk.word_tokenize(text)
    # print(tokens[:1000])

    # containing invalid chars
    regexp1 = re.compile("[^A-Za-z0-9-']")

    # containing only -- or - or numbers or ''
    regexp2 = re.compile("^-+$|^\d+$|^'+$")

    # extract words that match the
    validWords = filter(
        lambda x: not regexp1.search(x) and not regexp2.search(x), tokens
    )
    validWords = map(lambda x: x.lower(), validWords)

    # with open("unfiltered.txt", "w") as outfile:
    #     outfile.write("\n".join(validWords))

    # combine apostrophes
    apostropheWords = []
    for word in validWords:
        if "'" in word and "o'clock" not in word:
            apostropheWords[-1] += word
        else:
            apostropheWords.append(word)
    validWords = set(apostropheWords)
    print(validWords)

    with open("tokens.txt", "w") as outfile:
        # outfile.write("\n".join([token for token in tokens if not regexp.search(token)]))
        outfile.write("\n".join(validWords))


tokenize()
