class Garden:
    def __init__(
        self,
        diagram,
        students=[
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):

        self.students = sorted(students)
        diagram = diagram.split("\n")
        self.diagram = diagram

    def __get_plat_name(self, letter):
        plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
        return plants[letter]

    def plants(self, student):
        index = self.students.index(student)

        return list(
            self.__get_plat_name(p)
            for p in (
                self.diagram[0][index * 2 : index * 2 + 2]
                + self.diagram[1][index * 2 : index * 2 + 2]
            )
        )
