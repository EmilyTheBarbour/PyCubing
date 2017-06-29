from puzzle import Puzzle, Puzzles
import jsonpickle

puzzles = Puzzles()

f = open('puzzles.json', 'r')
puzzles = jsonpickle.decode(f.read())

puzzles.print_self()
