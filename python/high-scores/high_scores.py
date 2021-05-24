def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    three_highest = []

    for i in range(3):
        try:
            three_highest.append(scores.pop(scores.index(max(scores))))
        except ValueError:
            break

    return three_highest
