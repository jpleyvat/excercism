def is_pangram(sentence):
    letters = [i for i in range(97, 123)]
    for l in sentence:
        try:
            index = alphabet.index(ord(l.lower()))
            letters.pop(index)
        except (ValueError, IndexError):
            pass
    return len(letters) == 0
