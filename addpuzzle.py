import jsonpickle
from puzzle import Puzzle, Puzzles

puzzles = Puzzles()
puzzles.list.append(Puzzle("3x3"))
puzzles[0].add_shuffles('puzzles/3x3_shuffles.txt')
puzzles.default = puzzles.list[0]
puzzles.list.append(Puzzle("2x2"))
puzzles[1].add_shuffles('puzzles/2x2_shuffles.txt')
f = open('puzzles/puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()

print(len(puzzles))
for i, e in enumerate(puzzles):
    print("{}. {}".format(i + 1, e.name))

f = open('puzzles/puzzles.json', 'w')
f.write(jsonpickle.encode(puzzles))
f.close()
//test


