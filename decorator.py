import time


def decorator_times_3(func):
    def wrap_f(*args, **kwargs):
        start = time.time()
        print('Processing')
        rv = func(*args, **kwargs)
        end = time.time()
        print('Done function {}s in {}s'.format(str(func), end - start))
        # return times three
        return rv * 3

    return wrap_f


@decorator_times_3
def add(a, b):
    return a + b


@decorator_times_3
def long_time():
    start = time.time()
    print('Processing')
    time.sleep(2)
    return 0


print(add(1, 2))
long_time()
