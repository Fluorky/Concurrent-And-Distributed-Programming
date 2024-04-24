import os
from random import random
from typing import Tuple


def wire_pipes(from_: Tuple[int, int], to_: Tuple[int, int], f):
    os.close(from_[1])
    os.close(to_[0])
    with os.fdopen(from_[0], 'r') as r, os.fdopen(to_[1], 'w') as w:
        f(r, w)


n = int(random() * 200)


def parent(r, w):
    for i in range(n):
        x = 10*random()
        print(x, file=w)
        w.flush()
        y = float(r.readline())
        print(f'x = {x}, y = {y}')


def child(r, w):
    for i in range(n):
        x = float(r.readline())
        print(x*x, file=w)
        w.flush()


p0 = os.pipe()
p1 = os.pipe()

pid = os.fork()
if pid == 0:
    wire_pipes(p0, p1, child)
else:
    wire_pipes(p1, p0, parent)
    os.wait()