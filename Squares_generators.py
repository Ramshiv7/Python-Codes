# Generate the squares of the number till provided limit.

def sqr_gen(n):
    for i in range(n):
            yield i**2

for x in sqr_gen(10):
    print(x)
