class Puzzle:

    def __init__(self, name):
        self.name = name
        self.description,  = ""
        self.solves, self.shuffles = []

    def add_solve(self, solve):
        self.solves.append(solve)


three_by_three = Puzzle("3x3")
three_by_three.description = "A cuboid puzzle with 6 different colored faces who all rotate about their central cubie"
