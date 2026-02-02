class Matrix:
    def __init__(self, matrix_string: str):
        if "\n" in matrix_string:
            lines = matrix_string.split("\n")
        else:
            lines = [matrix_string]
        self.rows = [[] for _ in lines]
        for index, line in enumerate(lines):
            for num in line.split(" "):
                self.rows[index].append(int(num))

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.rows]
