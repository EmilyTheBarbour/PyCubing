from time import asctime

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
        self.shuffles = []

        self.session_solves = 0
        self.session_best = 9999
        self.session_average_of_three = 0
        self.session_average_of_five = 0
        self.session_average_of_twelve = 0
        self.session_average_of_hundred = 0

        self.overall_solves = []
        self.overall_best = 9999
        self.overall_average_of_three = 0
        self.overall_average_of_five = 0
        self.overall_average_of_twelve = 0
        self.overall_average_of_hundred = 0

    # a solve is a 3 item list, consistent of [time, shuffle, date_and_time]
    def add_solve(self, time, shuffle):
        self.session_solves += 1
        print(time)
        self.solves.append([time, shuffle, asctime()])
        self.session_best = min(self.session_best, time)
        if time < self.overall_best:
            print("new best! You beat your previous record by", self.overall_best - time, "seconds!")
            self.overall_best = time
        self.update_statistics()

    def update_statistics(self):
        print("")