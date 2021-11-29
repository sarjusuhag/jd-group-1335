from os import write
import nltk
import re

from nltk.util import tokenwrap


def tokenize():
    # download tokenization model
    nltk.download("punkt")

    # clean text
    text = None
    with open("./assets/text_to_parse/text.txt", encoding="cp1252") as file:
        text = file.read()
        # ignores special characters such as �
        # lowercases all characters
        text = text.encode("ascii", "ignore").decode().lower()

    # split text into tokens
    tokens = nltk.word_tokenize(text)

    # drop out words containing invalid chars
    regexp1 = re.compile("[^A-Za-z0-9-']")

    # drop out words containing only -- or - or numbers or ''
    regexp2 = re.compile("^-+$|^\d+$|^'+$")

    # extract words that match the
    validWords = filter(
        lambda x: not regexp1.search(x) and not regexp2.search(x), tokens
    )

    # combine apostrophes
    apostropheWords = []
    for word in validWords:
        if "'" in word and "o'clock" not in word:
            apostropheWords[-1] += word
        else:
            apostropheWords.append(word)
    validWords = sorted(set(apostropheWords))

    with open("./assets/out/tokens.txt", mode="w") as outfile:
        outfile.write("\n".join(validWords))


def write_nonrecorded():
    with open("./assets/out/tokens.txt", "r") as token_file, open(
        "./assets/text_to_parse/recorded_words.txt", "r"
    ) as recorded_words_file:
        tokens = set([line.rstrip() for line in token_file.readlines()])
        recorded_words = set(
            [line.rstrip("\n +") for line in recorded_words_file.readlines()]
        )

        to_record = sorted(tokens.difference(recorded_words))

        with open("./assets/out/to_record_words.txt", "w") as to_record_file:
            to_record_file.write("\n".join(to_record))


tokenize()
write_nonrecorded()
print("done!")
