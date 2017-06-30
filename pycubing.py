import time
import os
import jsonpickle
from puzzle import Solve
from userinterface import UI, OptionsPage

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
puzzles = jsonpickle.decode(f.read())
f.close()

# set the current working puzzle to the default puzzle loaded from the json file
current_puzzle = puzzles.default

# display some diagnostic information on startup
UI.display_start_up(version, puzzles, current_puzzle)
input()

# place holder main loop
# TODO: implement proper main loop
while True:

    # create a new solve
    current_solve = [0, current_puzzle.generate_shuffle(), time.asctime()]

    # place holder UI used to test core functionality; needs replacing
    # TODO: separate UI into it's own module; no UI management done outside this section
    UI.display_home(current_puzzle, current_solve)

    # place holder input validation for timer starting and stopping, as well as exiting when 1 is received
    # TODO: implement proper input detection

    # rudimentary input handling
    action = input()
    if action == "":
        start = time.time()
    elif action == 1:
        UI.display_options(OptionsPage.HOME)
    elif action == 0:
        break
    else:
        print("Error, unknown input, please try again.")

    input("press enter to stop time.")
    stop = time.time()
    current_solve[Solve.TIME] = round(stop - start, 2)

    # adds the resulting solve to the puzzle
    current_puzzle.add_solve(current_solve)

    # place holder used to pause UI refresh
    # TODO: implement separate UI module
    time.sleep(1)

# upon exit, populate json file with puzzles class, saving data
f = open('puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()
