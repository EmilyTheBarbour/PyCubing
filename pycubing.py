from time import time
from puzzle import Puzzle, Puzzles
import random
import jsonpickle

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
print("Puzzle:", current_puzzle.name)
print("Solves:", len(current_puzzle.solves))
print("Best:", current_puzzle.overall_best)
print("-----------------------------------------------------------------")
current_puzzle.add_solve(150, "shuffle")

# f = open('puzzles.json', 'w')
# f.write(jsonpickle.encode(puzzles))
# f.close()

