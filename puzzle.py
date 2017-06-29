from time import asctime
from bubblesort import bubble_sort
from functools import reduce

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
        self.session_best_of_five = 0
        self.session_best_of_twelve = 0
        self.session_best_of_hundred = 0

        self.overall_solves = []
        self.overall_best = 9999
        self.overall_average_of_three = 0
        self.overall_best_of_five = 0
        self.overall_best_of_twelve = 0
        self.overall_best_of_hundred = 0

    # a solve is a 3 item list, consistent of [time, shuffle, date_and_time]
    def add_solve(self, time, shuffle):
        self.session_solves += 1
        print(time)
        self.overall_solves.append([time, shuffle, asctime()])
        self.session_best = min(self.session_best, time)
        if time < self.overall_best:
            print("new best! You beat your previous record by", round(self.overall_best, 2) - time, "seconds!")
            self.overall_best = time
        self.update_statistics()

    def update_statistics(self):
        if self.session_solves >= 3:
            temp = []
            for e in self.overall_solves[-3:]:
                temp.append(e[0])
            self.session_average_of_three = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        if self.session_solves >= 5:
            temp = []
            for e in self.overall_solves[-5:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_five = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        if self.session_solves >= 12:
            temp = []
            for e in self.overall_solves[-12:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_five = round(reduce(lambda x, y: x + y, temp) / 10, 2)

        if self.session_solves >= 100:
            temp = []
            for e in self.overall_solves[-100:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_five = round(reduce(lambda x, y: x + y, temp) / 98, 2)


