def gen():
    for i in range(5):
        yield i

g = gen()
for i in range(5):
    print(next(g))
