class Puzzle:

    def __init__(self, name):
        self.name = name
        self.description  = ""
        self.solves = []
        self.shuffles = []

    #a solve is a 2 item list, consistent of [time, shuffle]
    def add_solve(self, solve):
        self.solves.append(solve)



three_by_three = Puzzle("3x3")
three_by_three.description = "A cuboid puzzle with 6 different colored faces who all rotate about their central cubie"
three_by_three.add_solve([5.5,"test"])
three_by_three.add_solve([5.5,"test"])
three_by_three.print_solves()