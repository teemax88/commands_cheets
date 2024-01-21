def generator():
    for i in range(3):
        x = yield i
        print(x)

g = generator()
print(next(g))
print(next(g))
g.send("foo bar!")
print(next(g))
# print(next(g))
# print(next(g))
raise StopIteration
