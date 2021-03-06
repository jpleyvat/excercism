from collections import Counter


def total(basket: list):
    final_price = 0
    books_diff = []
    cost = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}

    if not set(basket).issubset({1, 2, 3, 4, 5}):
        raise Exception(
            "Please insert only the valid books. Valid books are: 1, 2, 3, 4, 5."
        )

    while len(basket) > 0:
        basket_set = set(basket)
        books_diff.append(len(basket_set))
        for i in basket_set:
            basket.remove(i)

    while 5 in books_diff and 3 in books_diff:
        books_diff[books_diff.index(5)] = 4
        books_diff[books_diff.index(3)] = 4

    for i in books_diff:
        final_price += cost[i]

    return final_price
