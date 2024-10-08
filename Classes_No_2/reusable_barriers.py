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

class ReusableBarrier:
    def __init__(self,  n):
        self.gate1 = Gate(False)
        self.gate2 = Gate(True)
        self.n = n
        self.m = n
        self.lock = RLock()
    def tryPass1(self):
        with self.lock:
            self.m -= 1
            if self.m == 0:
                self.gate2.close()
                self.gate1.open()
        self.gate1.tryPass()
    def tryPass2(self):
        with self.lock:
            self.m += 1
            if self.m == self.n:
                self.gate1.close()
                self.gate2.open()
        self.gate2.tryPass()

class MyThread(Thread):
    def __init__(self, m):
        Thread.__init__(self)
        self.m = m
    def run(self):
        for _ in range(5):
            sleep(random())
            print('Thread', self.m, 'executed A')
            barrier.tryPass1()
            sleep(random())
            print('Thread', self.m, 'executed B')
            barrier.tryPass2()

n_threads = 10
barrier = ReusableBarrier(n_threads)
for m in range(n_threads):
    MyThread(m).start()