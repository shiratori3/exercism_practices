class Garden:
    PLANTS = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }

    def __init__(self, diagram: str,
                 students: list[str] = [
                        "Alice", "Bob", "Charlie", "David",
                        "Eve", "Fred", "Ginny", "Harriet",
                        "Ileana", "Joseph", "Kincaid", "Larry"
                    ]):
        self.graden = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, name: str):
        index = self.students.index(name) * 2
        res = [
            self.graden[0][index],
            self.graden[0][index + 1],
            self.graden[1][index],
            self.graden[1][index + 1],
        ]
        return [Garden.PLANTS.get(char) for char in res]
