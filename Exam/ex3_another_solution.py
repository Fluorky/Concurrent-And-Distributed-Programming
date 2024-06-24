import threading as th
import random as r

X = 10.0
lock = th.Lock()
condition = th.Condition(lock)
semaphore = th.Semaphore(1)


class Adder(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            with condition:
                while X >= 30.0:
                    condition.wait()
                increment = r.random() * 10.0
                X += increment
                print(f"Added {increment:.2f}, X = {X:.2f}")
                condition.notify_all()
                semaphore.release()


class Subtr(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        global X
        while True:
            with condition:
                while X <= 10.0:
                    condition.wait()
                decrement = r.random() * 10.0
                X -= decrement
                print(f"Subtracted {decrement:.2f}, X = {X:.2f}")
                condition.notify_all()
                semaphore.release()


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
