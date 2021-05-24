def is_isogram(string):
    string = string.replace("-", "").replace(" ", "").lower()
    p = []
    for c in string:
        p.append(c)

    return not (False in [p.count(c) == 1 for c in string])
