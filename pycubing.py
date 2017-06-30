import time
import os
import jsonpickle
from puzzle import Solve

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
f = open('puzzles.json', 'r')
puzzles = jsonpickle.decode(f.read())
f.close()

# set the current working puzzle to the default puzzle loaded from the json file
current_puzzle = puzzles.default

# place holder variable to cause main program to loop until exit is desired
# TODO: implement proper main loop
quit_loop = 0

# place holder main loop
# TODO: implement proper main loop
while quit_loop == 0:

    current_solve = [0, current_puzzle.generate_shuffle(), time.asctime()]

    # Intended to clear the console so that the text is displayed in the same place every time
    os.system('cls')

    # place holder UI used to test core functionality; needs replacing
    # TODO: separate UI into it's own module; no UI management done outside this section
    print("Session of", time.strftime("%B %d, %Y", time.localtime()))
    print(len(current_puzzle.shuffles), "Shuffles loaded.")
    print("-----------------------------------------------------------------")
    print("Puzzle:", current_puzzle.name)
    print("Solves:", current_puzzle.session_solves)
    print("Best:  ", current_puzzle.overall_best)
    if current_puzzle.session_solves >= 3  : print("Ao3:   ", current_puzzle.session_average_of_three)
    if current_puzzle.session_solves >= 5  : print("Bo5:   ", current_puzzle.session_best_of_five)
    if current_puzzle.session_solves >= 12 : print("Bo12:  ", current_puzzle.session_best_of_twelve)
    if current_puzzle.session_solves >= 100: print("Bo100: ", current_puzzle.session_best_of_hundred)
    print("-----------------------------------------------------------------\n")
    print(current_solve[Solve.SHUFFLE])

    # place holder input validation for timer starting and stopping, as well as exiting when 1 is received
    # TODO: implement proper input detection
    if input("press enter to start time. press 1 to end ") == "1":
        break

    start = time.time()
    input("press enter to stop time.")
    stop = time.time()

    # adds the resulting time and shuffle to the puzzle for handling
    current_puzzle.add_solve(current_solve)

    # place holder used to pause UI refresh
    # TODO: implement separate UI module
    time.sleep(1)

# upon exit, populate json file with puzzles class, saving data
f = open('puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()

