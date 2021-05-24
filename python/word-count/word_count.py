def is_letter_or_number(char):
    return char.isdigit() or char.isalpha()


def count_words(sentence):
    sentence = sentence.lower()
    splited_sentence = []
    word = ""

    for i, l in enumerate(sentence):
        if is_letter_or_number(l):
            word += l
            continue

        if l == "'":
            try:
                if is_letter_or_number(sentence[i - 1]) and is_letter_or_number(
                    sentence[i + 1]
                ):
                    word += l
                    continue
            except IndexError:
                pass
        splited_sentence.append(word)
        word = ""
        continue
    splited_sentence.append(word)

    return {
        word: splited_sentence.count(word) for word in splited_sentence if word != ""
    }
