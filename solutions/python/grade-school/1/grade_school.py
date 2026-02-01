class School:
    def __init__(self):
        self.students = {}
        self.students_added = []

    def add_student(self, name: str, grade: int) -> None:
        if name not in self.students.keys():
            self.students[name] = grade
            self.students_added.append(True)
        else:
            self.students_added.append(False)

    def roster(self):
        return sorted(self.students.keys(),
                      key=lambda name: (self.students[name], name))

    def grade(self, grade_number):
        return sorted([k for k, v in self.students.items()
                       if v == grade_number])

    def added(self) -> list[bool]:
        return self.students_added
