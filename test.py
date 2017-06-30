from puzzle import Puzzle

x = Puzzle("test")
x.add_shuffles('3x3_shuffles.txt')

print(len(x.shuffles))
print(x.generate_shuffle())
