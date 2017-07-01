import time
import os
import jsonpickle
from puzzle import Solve, Puzzles
from userinterface import UI, OptionsPage
from options import Options

version = "0.5"

# time is used to generate date_times for session logging, and time() for timing solves (stop - start)
# os is intended to be used for clearing the screen, although this functionality is currently nonworking
# jsonpickle is the module for encoding and decoding object structures into json files: used for puzzles

# region
# place holder code to reset json file as well as initialize new fields
# from puzzle import Puzzle, Puzzles
# puzzles = Puzzles()
# puzzles.list.append(Puzzle("3x3"))
# puzzles.default = puzzles.list[0]
# f = open('puzzles.json', 'w')
# f.write(jsonpickle.encode(puzzles))
# f.close()
# endregion


# open stream reader to puzzles json file, generating the puzzles class from said file
f = open('puzzles/puzzles.json', 'r')
puzzles_buffer = jsonpickle.decode(f.read())
f.close()

puzzles = Puzzles()
for e in puzzles_buffer:
    if e not in puzzles:
        puzzles.append(e)
puzzles.default = puzzles_buffer.default

print(puzzles[0].shuffles)
print(puzzles.default)

# set the current working puzzle to the default puzzle loaded from the json file
# TODO: find a better way to initialize session information such that it doesn't come from / save to json
current_puzzle = puzzles.default
current_puzzle.session_solves = 0
current_puzzle.session_best = 9999
current_puzzle.session_average_of_three = 0
current_puzzle.session_best_of_five = 0
current_puzzle.session_best_of_twelve = 0
current_puzzle.session_best_of_hundred = 0

# display some diagnostic information on startup
UI.display_start_up(version, puzzles, current_puzzle)
input()

# place holder main loop
# TODO: implement proper main loop
while True:

    # create a new solve
    current_solve = [0, current_puzzle.generate_shuffle(), time.asctime()]
    old_best = current_puzzle.overall_best

    # place holder UI used to test core functionality; needs replacing
    # TODO: separate UI into it's own module; no UI management done outside this section
    UI.display_home(current_puzzle, current_solve)

    # place holder input validation for timer starting and stopping, as well as exiting when 1 is received
    # TODO: implement proper input detection

    # rudimentary input handling
    action = input()
    if action == "":
        start = time.time()
        UI.clear()
        input("press enter to stop time.")
        stop = time.time()
        current_solve[Solve.TIME] = round(stop - start, 2)

        # adds the resulting solve to the puzzle, getting all of the different statistics changed in return
        solve_results = current_puzzle.add_solve(current_solve)

        UI.display_solve_results(current_solve, solve_results)

    elif action == "1":
        Options.show(current_puzzle, puzzles)
        current_puzzle = Options.current_puzzle_out
        puzzles = Options.puzzles_out
    elif action == "0":
        break
    else:
        UI.display_error(0x000001)
        input()

# upon exit, populate json file with puzzles class, saving data
f = open('puzzles/puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()
