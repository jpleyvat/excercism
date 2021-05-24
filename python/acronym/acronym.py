from string import punctuation


def abbreviate(words):
    words = words.translate(
        str.maketrans({**dict.fromkeys(punctuation.replace("'", " "), " ")})
    )
    words = words.split(" ")
    return "".join([word[0].upper() for word in words if len(word) > 0])
