class Puzzle:

    def __init__(self, name):
        self.name = name
        self.description,  = ""
        self.solves, self.shuffles = []

    def add_solve(self, solve):
        self.solves.append(solve)

class Solve:

    def __init__(self, time, shuffle):
        self.time = time
        self.shuffle = shuffle


three_by_three = Puzzle("3x3")
three_by_three.description = "A cuboid puzzle with 6 different colored faces who all rotate about their central cubie"
three_by_three.add_solve(Solve(5.5,"test"))

print(three_by_three.solves)