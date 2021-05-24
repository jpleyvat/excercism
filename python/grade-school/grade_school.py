class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if not str(grade) in self.grades.keys():
            self.grades[str(grade)] = []

        self.grades[str(grade)].append(name)
        self.grades[str(grade)].sort()

    def roster(self):
        return [
            student for grade in sorted(self.grades.items()) for student in grade[1]
        ]

    def grade(self, grade_number):
        try:
            return self.grades[str(grade_number)]
        except KeyError:
            return []
