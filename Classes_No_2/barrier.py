from threading import Thread, Condition, RLock
from time import sleep
from random import random

class Gate:
    def __init__(self, is_open = False):
        self.cond = Condition()
        self.is_open = is_open
    def open(self):
        with self.cond:
            self.is_open = True
            self.cond.notify_all()
    def close(self):
        with self.cond:
            self.is_open = False
    def tryPass(self):
        with self.cond:
            self.cond.wait_for(lambda:self.is_open)

class Barrier:
    def __init__(self, n):
        self.lock = RLock()
        self.gate = Gate()
        self.m = n
    def tryPass(self):
        with self.lock:
            self.m -= 1
            if self.m == 0:
                self.gate.open()
        self.gate.tryPass()

class MyThread(Thread):
    def __init__(self, m):
        Thread.__init__(self)
        self.m = m
    def run(self):
        sleep(random())
        print('Thread', self.m, 'executed A')
        barrier.tryPass()
        sleep(random())
        print('Thread', self.m, 'executed B')

n_threads = 10
barrier = Barrier(n_threads)
for m in range(n_threads):
    MyThread(m).start()