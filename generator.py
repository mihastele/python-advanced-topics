# generator doesn't store the values in memory, it yields one value at a time

class ITimesGenerator:
    def __init__(self, n):
        # 2 state variables store less memory than a complete list
        self.n = n
        self.last = 0

    # call next() each time the generator is called
    def __next__(self):
        return self.next()

    # make it an iterable
    def __iter__(self):
        return self

    # next() yields the next value and increases its counter where it compares the counter to the limit
    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv


generator = ITimesGenerator(10)

for i in generator:
    print(i)

import sys
def gen(n):
    for i in range(n):
        # yield pauses the function and returns the value
        # yield waits until the function is called again then it continues
        # return would be the stop of the function
        yield i ** 2


for i in gen(10):
    print(i)

# new generators always start at the beginning
print(next(gen(10)))
print(next(gen(10)))
print(next(gen(10)))

# the generator is stored in the variable to be more useful
g = gen(10)
print(next(g))
print(next(g))
print(next(g))

x = [i ** 2 for i in range(1000)]
y = gen(1000)
print(sys.getsizeof(x))
print(sys.getsizeof(y))