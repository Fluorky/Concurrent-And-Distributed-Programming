import os, random

class Window:
    def __init__(self, size):
        self.size = size
        self.buf = [0 for i in range(size)]
        self.pos = 0
    def add(self, x):
        self.buf[self.pos] = x
        self.pos = (self.pos + 1) % self.size
        return sum(self.buf)

r, w = os.pipe()

if os.fork() > 0:
    os.close(r)
    w = os.fdopen(w, "w")
    for i in range(100):
        print(10 * random.random(), file = w)
        w.flush()
    w.close()
    os.wait()
    print('Koniec')
else:
    os.close(w)
    win_sum = Window(5)
    with os.fdopen(r, "r") as r:
        for x in r:
            res = win_sum.add(float(x))
            print('x=', float(x),' res=', res)