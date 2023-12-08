import io


# file = open('file.txt', 'r')
# file.write('Hello, World!')
# # issue exists when we don't reach the close
# raise Exception('Something went wrong!')
# file.close()

# solution 1
# file = file = open('file.txt', 'r')
# try:
#     file.write('Hello, World!')
# finally:
#     file.close()
#
# with open('file.txt', 'r') as file:
#     file.write('Hello, World!')
#     raise Exception('Something went wrong!')
#


class FileWithCtxManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        print('enter')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'exc_traceback: {exc_traceback}')
        print('exit')
        self.file.close()

        if exc_type == io.UnsupportedOperation:
            # return True tells python that we gracefully handled the exception and it doesn't need to raise it
            return True
        return False


with FileWithCtxManager('file.txt', 'r') as file:
    print('middle')
    # fail block below since there is a read mode not write
    file.write('Hello, World!')

# with FileWithCtxManager('file.txt', 'r') as file:
#     # This one will crash
#     raise Exception('Something went wrong!')

## context manager with generator
import contextlib


@contextlib.contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()
    print('exit')


import threading

class LockedResource:
    def __init__(self, resource):
        self.lock = threading.Lock()
        self.resource = resource

    def __enter__(self):
        self.lock.acquire()
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.lock.release()

import time

resource = {}
lr = LockedResource(resource)

def worker1(resource):
    with lr as r:
        print("Worker 1 is working...")
        r["key"] = "value1"
        time.sleep(1)  # Simulate some work
        print("Worker 1 finished.")

def worker2(resource):
    with lr as r:
        print("Worker 2 is working...")
        r["key"] = "value2"
        time.sleep(1)  # Simulate some work
        print("Worker 2 finished.")


thread1 = threading.Thread(target=worker1, args=(resource,))
thread2 = threading.Thread(target=worker2, args=(resource,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(resource)