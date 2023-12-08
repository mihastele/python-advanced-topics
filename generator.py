
# generator doesn't store the values in memory, it yields one value at a time

class ITimesGenerator:
    def __init__(self, n):
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