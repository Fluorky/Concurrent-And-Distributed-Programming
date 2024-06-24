import threading as th
import random as r

X = 10.0
mutex = th.Lock()
can_add = th.Condition(mutex)
can_sub = th.Condition(mutex)


class Adder(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            with can_add:
                while X >= 30.0:
                    can_add.wait()
                value = r.random() * 10.0
                X += value
                print(f"Adder: Added {value:.2f}, new X = {X:.2f}")
                can_sub.notify_all()


class Subtr(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            with can_sub:
                while X <= 10.0:
                    can_sub.wait()
                value = r.random() * 10.0
                X -= value
                print(f"Subtr: Subtracted {value:.2f}, new X = {X:.2f}")
                can_add.notify_all()


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
