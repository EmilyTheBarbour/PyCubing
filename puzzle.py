from bubblesort import bubble_sort
from functools import reduce
import random

# bubblesort is used to sort the list of times in statistical analysis (for example best of 5) so that
# the fastest and slowest times can be removed
# reduce is used to implement a lambda function that adds all items of a list together such that it can be divided
# by its length


# enumeration of Solve list positons
class Solve:
    TIME, SHUFFLE, DATE_TIME = range(0, 3)


# enumeration of potential Solve Results
class SolveResults:
    NEW_OVERALL_BEST = 0
    NEW_SESSION_BEST = 1


# class structure used mainly for organizing all of the objects for json encoding and decoding
class Puzzles:
    def __init__(self):
        # list of all the used puzzles
        self.list = []
        # default Puzzle used on load
        self.default = Puzzle("default")

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        for e in self.list:
            yield e


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
    def add_solve(self, solve):
        self.session_solves += 1

        # generate list of solve information and append it to overall solves list
        self.overall_solves.append(solve)

        # Update statistics
        solve_results = self.update_statistics(solve)
        return solve_results

    # used to update statistics; currently only handling session statistics
    # all parts use a temp list so that a list of only the time component of a solve is generated
    # TODO: implement overall statistics management, only perform one bubble sort for more efficiency
    def update_statistics(self, solve):
        # list of all the different updates to statistics for UI to parse, as well as a value to display if desired
        solve_results = []

        # determine if session best has been beaten and add that to solve_results
        if solve[Solve.TIME] < self.session_best:
            solve_results.append([SolveResults.NEW_SESSION_BEST,
                                  round(self.session_best - solve[Solve.TIME], 2)])
            self.session_best = solve[Solve.TIME]

        # determine if overall best has been beaten and add that to solve_results
        if solve[Solve.TIME] < self.overall_best:
            solve_results.append([SolveResults.NEW_OVERALL_BEST,
                                  round(self.overall_best - solve[Solve.TIME], 2)])
            self.overall_best = solve[Solve.TIME]

        # TODO: fix only doing 2 bubble sorts as this does not represent proper statistics, make each check do it
        # generate sorted solves that each statistic uses, done so that only one bubble sort is called
        # only works with last 100 since no statistic requires more
        sorted_solves = []
        for e in self.overall_solves[-min(self.session_solves, 100):]:
            sorted_solves.append(e[Solve.TIME])
        sorted_solves = bubble_sort(sorted_solves)

        # Session Average of 3 computation
        if self.session_solves >= 3:
            temp = sorted_solves[-3:]
            self.session_average_of_three = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # Session Best of 5
        if self.session_solves >= 5:
            temp = sorted_solves[-5:]
            temp.pop(0)
            temp.pop(-1)
            self.session_best_of_five = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # Session Best of 12
        if self.session_solves >= 12:
            temp = sorted_solves[-12:]
            temp.pop(0)
            temp.pop(-1)
            self.session_best_of_twelve = round(reduce(lambda x, y: x + y, temp) / 10, 2)

        # Session Best of 100
        if self.session_solves >= 100:
            temp = sorted_solves
            temp.pop(0)
            temp.pop(-1)
            self.session_best_of_hundred = round(reduce(lambda x, y: x + y, temp) / 98, 2)

        # regenerate for overall
        for e in self.overall_solves[-min(len(self.overall_solves), 100):]:
            sorted_solves.append(e[Solve.TIME])
        sorted_solves = bubble_sort(sorted_solves)

        # Overall Average of 3 computation
        if len(self.overall_solves) >= 3:
            temp = sorted_solves[-3:]
            self.overall_average_of_three = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # Overall Best of 5
        if len(self.overall_solves) >= 5:
            temp = sorted_solves[-5:]
            temp.pop(0)
            temp.pop(-1)
            self.overall_best_of_five = round(reduce(lambda x, y: x + y, temp) / 3, 2)

        # Overall Best of 12
        if len(self.overall_solves) >= 12:
            temp = sorted_solves[-12:]
            temp.pop(0)
            temp.pop(-1)
            self.overall_best_of_twelve = round(reduce(lambda x, y: x + y, temp) / 10, 2)

        # Overall Best of 100
        if len(self.overall_solves) >= 100:
            temp = sorted_solves
            temp.pop(0)
            temp.pop(-1)
            self.overall_best_of_hundred = round(reduce(lambda x, y: x + y, temp) / 98, 2)

        return solve_results
