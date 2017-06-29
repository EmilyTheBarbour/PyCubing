import time
import os
import jsonpickle
from puzzle import Puzzle, Puzzles

# puzzles = Puzzles()
# puzzles.list.append(Puzzle("3x3"))
# puzzles.default = puzzles.list[0]
# f = open('puzzles.json', 'w')
# f.write(jsonpickle.encode(puzzles))
# f.close()

f = open('puzzles.json', 'r')
puzzles = jsonpickle.decode(f.read())
f.close()

current_puzzle = puzzles.default
quit = 0

while quit == 0:

    os.system('cls')
    print("Session of", time.strftime("%B %d, %Y", time.localtime()))
    print("-----------------------------------------------------------------")
    print("Puzzle:", current_puzzle.name)
    print("Solves:", current_puzzle.session_solves)
    print("Best:  ", current_puzzle.overall_best)
    if current_puzzle.session_solves >= 3  : print("Ao3:   ", current_puzzle.session_average_of_three)
    if current_puzzle.session_solves >= 5  : print("Ao5:   ", current_puzzle.session_average_of_five)
    if current_puzzle.session_solves >= 12 : print("Ao12:  ", current_puzzle.session_average_of_twelve)
    if current_puzzle.session_solves >= 100: print("Ao100: ", current_puzzle.session_average_of_hundred)
    print("-----------------------------------------------------------------\n")

    if input("press enter to start time. press 1 to end ") == "1": break
    start = time.time()
    input("press enter to stop time.")
    stop = time.time()

    current_puzzle.add_solve(round(stop - start, 2), "shuffle")

    time.sleep(1)


f = open('puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()

