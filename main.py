from os import write
import nltk
import re

from nltk.util import tokenwrap


def tokenize():
    # download tokenization model
    nltk.download("punkt")

    # clean text
    text = None
    with open("./assets/frederick_douglass_text.txt", encoding="cp1252") as file:
        text = file.read()
        # ignores special characters such as �
        # lowercases all characters
        text = text.encode("ascii", "ignore").decode().lower()

    tokens = nltk.word_tokenize(text)

    # containing invalid chars
    regexp1 = re.compile("[^A-Za-z0-9-']")

    # containing only -- or - or numbers or ''
    regexp2 = re.compile("^-+$|^\d+$|^'+$")

    # extract words that match the
    validWords = filter(
        lambda x: not regexp1.search(x) and not regexp2.search(x), tokens
    )
    validWords = map(lambda x: x.lower(), validWords)

    # combine apostrophes
    apostropheWords = []
    for word in validWords:
        if "'" in word and "o'clock" not in word:
            apostropheWords[-1] += word
        else:
            apostropheWords.append(word)
    validWords = sorted(set(apostropheWords))

    with open("tokens.txt", "w") as outfile:
        # outfile.write("\n".join([token for token in tokens if not regexp.search(token)]))
        outfile.write("\n".join(validWords))


def write_nonrecorded():
    with open("tokens.txt", "r") as token_file, open(
        "./assets/recorded_words.txt", "r"
    ) as recorded_words_file:
        tokens = set([line.rstrip() for line in token_file.readlines()])
        recorded_words = set(
            [line.rstrip("\n +") for line in recorded_words_file.readlines()]
        )

        to_record = sorted(tokens.difference(recorded_words))

        with open("to_record_words.txt", "w") as to_record_file:
            to_record_file.write("\n".join(to_record))


tokenize()
write_nonrecorded()
print("done!")
