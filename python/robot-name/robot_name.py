from random import randint

robots = []


class Robot:
    def __init__(self):
        self.__set_name()

    def __set_name(self):
        while True:
            name = self.__get_random_name()
            if not name in robots:
                self.name = name
                robots.append(name)
                break

    def __get_random_name(self):
        return "".join(
            (
                chr(randint(65, 91)),
                chr(randint(65, 91)),
                str(randint(0, 9)),
                str(randint(0, 9)),
                str(randint(0, 9)),
            )
        )

    def reset(self):
        self.__set_name()
