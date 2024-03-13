import multiprocessing
from multiprocessing import Queue
from queue import Empty
from time import sleep
from random import random


def f(q: Queue):
    for i in range(1, 2):
        sleep(random())
        q.put((i, random()))


if __name__ == '__main__':
    q = Queue()
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    i = -1
    print('Main')

    while i<10:
        sleep(1)
        try:
            i, x = q.get(timeout=0.1)
            print(f'i={i}, x = {x}')
        except Empty:
            print('Timeout')
  