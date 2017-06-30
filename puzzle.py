from time import asctime
from bubblesort import bubble_sort
from functools import reduce

# bubblesort is used to sort the list of times in statistical analysis (for example best of 5) so that
# the fastest and slowest times can be removed
# reduce is used to implement a lambda function that adds all items of a list together such that it can be divided
# by its length

# class structure used mainly for organizing all of the objects for json encoding and decoding
class Puzzles:
    def __init__(self):
        # list of all the used puzzles
        self.list = []
        # default Puzzle used on load
        self.default = Puzzle("default")

# main class structure used for holding information for each of the different puzzles in use
class Puzzle:

    def __init__(self, name):
        # core information about the puzzle
        self.name = name
        self.description  = ""
        self.shuffles = []

        # statistics related to the current session
        self.session_solves = 0
        self.session_best = 9999
        self.session_average_of_three = 0
        self.session_best_of_five = 0
        self.session_best_of_twelve = 0
        self.session_best_of_hundred = 0

        # statistics related to the overall performance
        self.overall_solves = []
        self.overall_best = 9999
        self.overall_average_of_three = 0
        self.overall_best_of_five = 0
        self.overall_best_of_twelve = 0
        self.overall_best_of_hundred = 0

    # a solve is a 3 item list, consistent of [float time, string shuffle, string date_and_time]
    # date time is in the format of "abDoW abMonth day HH:MM:SS year"
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

            self.session_best_of_twelve = round(reduce(lambda x, y: x + y, temp) / 10, 2)

        if self.session_solves >= 100:
            temp = []
            for e in self.overall_solves[-100:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_hundred = round(reduce(lambda x, y: x + y, temp) / 98, 2)


