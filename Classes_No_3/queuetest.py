import threading
from queue import Queue
from time import sleep
from random import random


def f(q: Queue):
    for i in range(1, 100):
        sleep(random())
        q.put((i, random()))


if __name__ == '__main__':
    q = Queue()
    th = threading.Thread(target=f, args=(q,))
    th.start()
    while True:
        i, x = q.get(timeout=0.1)
        print(f'i={i}, x = {x}')
