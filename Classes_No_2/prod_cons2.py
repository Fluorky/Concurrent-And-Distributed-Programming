from threading import Thread, Condition
from time import sleep
from random import random

class MyQueue:
    def __init__(self):
        self._buf = []
        self.cond = Condition()
    def enqueue(self, x):
        with self.cond:
            self._buf.append(x)
            self.cond.notify()
    def dequeue(self):
        with self.cond:
            self.cond.wait_for(lambda:self._buf)
            return self._buf.pop(0)
    def __str__(self):
      return f'Queue<{self._buf}>'
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

queue = MyQueue()
threads = [Producer(queue, n) for n in range(10)]
threads += [Consumer(queue, n) for n in range(10)]

for t in threads:
    t.start()