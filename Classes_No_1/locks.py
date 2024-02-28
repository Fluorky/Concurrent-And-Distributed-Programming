from threading import Thread, RLock
from time import sleep
from random import random

counter = 0
lock = RLock()


def count():
    global counter
    sleep(5 * random())
    lock.acquire()  # we acquire lock before modifying the counter
    x = counter + 1
    # raise Exception('hello')
    sleep(random())
    counter = x
    lock.release()  # we release the lock after modifying the counter
    print(x)


threads = [Thread(target=count) for i in range(20)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'Threads finished, counter={counter}')
