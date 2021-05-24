class Matrix:
    def __init__(self, matrix_string):
        self.rows = tuple(
            [
                list(int(number) for number in row.split(" "))
                for row in matrix_string.split("\n")
            ]
        )
        self.colums = tuple(list(column) for column in zip(*self.rows))

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.colums[index - 1]
