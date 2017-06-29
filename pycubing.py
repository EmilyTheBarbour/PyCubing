from puzzle import Puzzle
import jsonpickle

#structured such that first item in list is preferred puzzle on startup
puzzles = []

f = open('puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
