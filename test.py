from puzzle import Puzzle

x = Puzzle("test")
f = open('3x3_shuffles.txt', 'r')
x.add_shuffles(f.read())
f.close()

print(x.shuffles)
print(x.generate_shuffle())
