from threading import RLock, Condition, Thread
from time import sleep
from random import random

class MyQueue:
    def __init__(self,size):
        self.size = size
        self._buf = [None] * size
        self.wpos = 0
        self.rpos = 0
        self.count = 0
        lock = RLock()
        self.empty = Condition(lock)
        self.full = Condition(lock)
    def enqueue(self, x):
        with self.full:
            self.full.wait_for(lambda:self.count<self.size)
            self._buf[self.wpos] = x
            self.count += 1
            self.wpos = (self.wpos + 1) % self.size
            self.empty.notify()
    def dequeue(self):
        with self.empty:
            self.empty.wait_for(lambda:self.count>0)
            el = self._buf[self.rpos]
            self.count -= 1
            self.rpos = (self.rpos + 1) % self.size
            self.full.notify()
        return el
    def __str__(self):
      return f'Queue<{self._buf}, count={self.count}, rpos={self.rpos}, wpos={self.wpos}>'

class Producer(Thread):
    def __init__(self, queue, n):
        Thread.__init__(self)
        self.queue = queue
        self.n = n
    def run(self):
        for i in range(10):
            sleep(random())
            print(f'Producer {self.n}, iteration {i}, {self.queue}')
            self.queue.enqueue((self.n, i))

class Consumer(Thread):
    def __init__(self, queue, n):
        Thread.__init__(self)
        self.queue = queue
        self.n = n
    def run(self):
        for i in range(10):
            sleep(random())
            print(f'Consumer {self.n} starts to consume')
            msg = self.queue.dequeue()
            print(f'Consumer {self.n}, iteration {i}, msg={msg}, {self.queue}')

queue = MyQueue(2)
threads = [Producer(queue, n) for n in range(10)]
threads += [Consumer(queue, n) for n in range(10)]

for t in threads:
    t.start()