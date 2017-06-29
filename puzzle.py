class Puzzles:
    def __init__(self):
        self.list = []
        self.default = Puzzle("default")


    def print_self(self):
        print(vars(self.default))
        print([(i, vars(j)) for i, j in enumerate(self.list)])

class Puzzle:

    def __init__(self, name):
        self.name = name
        self.description  = ""
        self.solves = []
        self.shuffles = []
        self.best = 0
        self.average_of_three = 0
        self.average_of_five = 0
        self.average_of_twelve = 0
        self.average_of_hundred = 0

    #a solve is a 3 item list, consistent of [time, shuffle, date_and_time]
    def add_solve(self, solve):
        self.solves.append(solve)
