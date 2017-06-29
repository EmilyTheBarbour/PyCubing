

class Puzzles:
    def __init__(self):
        self.list = []
        self.default = ''

    def print_self(self):
        print(vars(self.default))
        print([(i, vars(j)) for i, j in enumerate(self.list)])

class Puzzle:

    def __init__(self, name):
        self.name = name
        self.description  = ""
        self.solves = []
        self.shuffles = []


    #a solve is a 2 item list, consistent of [time, shuffle]
    def add_solve(self, solve):
        self.solves.append(solve)
