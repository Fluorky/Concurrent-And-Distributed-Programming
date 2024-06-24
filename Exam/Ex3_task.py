import threading as th
import random as r

X = 10.0


class Adder(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            X = X + r.random() * 10.0
            print(f"Adder:  new X = {X:.2f}")


class Subtr(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            X = X - r.random() * 10.0
            print(f"Subtr:  new X = {X:.2f}")


def factory():
    if r.random() < 0.5:
        return Adder()
    else:
        return Subtr()


ths = [factory() for i in range(10)]

for t in ths:
    t.start()

for t in ths:
    t.join()
