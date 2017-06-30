from time import asctime
from bubblesort import bubble_sort
from functools import reduce
import random

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

    def __getitem__(self, item):
        return self.list[item]


# main class structure used for holding information for each of the different puzzles in use
class Puzzle:

    def __init__(self, name):
        # core information about the puzzle
        self.name = name
        self.description = ""
        self.shuffles = []
        self.shuffles_file = ""

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
        self.overall_session_date_and_times = []

    # a shuffle is a string containing moves separated by spaces; each shuffle is itself separated by a new line
    def add_shuffles(self, file):
        self.shuffles_file = file
        f = open(file, 'r')
        self.shuffles.extend(f.read().split('\n'))
        f.close()

    # returns a random shuffle from the list of shuffles; can be expanded to an algorithm in the future
    def generate_shuffle(self):
        return self.shuffles[random.randint(0, len(self.shuffles) - 1)]

    # a solve is a 3 item list, consistent of [float time, string shuffle, string date_and_time]
    # date time is in the format of "abDoW abMonth day HH:MM:SS year"
    def add_solve(self, time, shuffle):
        self.session_solves += 1

        # place holder for printing time
        # TODO: to be moved to main UI handling
        print(time)

        # generate list of solve information and append it to overall solves list
        self.overall_solves.append([time, shuffle, asctime()])

        # assign session best to the minimum time between session best and current solve time: will not be broadcast
        self.session_best = min(self.session_best, time)

        # place holder for determining if user got a new personal best;
        # TODO: split such that add_solve returns a value
        # TODO: that can be used to infer any extra information by the UI handling
        if time < self.overall_best:
            print("new best! You beat your previous record by", round(self.overall_best, 2) - time, "seconds!")
            self.overall_best = time

        #
        self.update_statistics()

    # used to update statistics; currently only handling session statistics
    # all parts use a temp list so that a list of only the time component of a solve is generated
    # TODO: implement overall statistics management, only perform one bubble sort for more efficiency
    def update_statistics(self):
        # Average of 3 computation
        if self.session_solves >= 3:
            temp = []
            for e in self.overall_solves[-3:]:
                temp.append(e[0])
            self.session_average_of_three = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # All of the Best of x computations follow the same format:
        # generate temp list of last x solves, sort them using a bubble sort, and pop off the lowest and highest time
        # then take the statistical mean and report

        # Best of 5
        if self.session_solves >= 5:
            temp = []
            for e in self.overall_solves[-5:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_five = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # Best of 12
        if self.session_solves >= 12:
            temp = []
            for e in self.overall_solves[-12:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_twelve = round(reduce(lambda x, y: x + y, temp) / 10, 2)
        # Best of 100
        if self.session_solves >= 100:
            temp = []
            for e in self.overall_solves[-100:]:
                temp.append(e[0])
            temp = bubble_sort(temp)
            temp.pop(0)
            temp.pop(-1)

            self.session_best_of_hundred = round(reduce(lambda x, y: x + y, temp) / 98, 2)


