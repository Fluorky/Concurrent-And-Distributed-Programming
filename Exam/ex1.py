import threading
import random


class MyThread(threading.Thread):
    def __init__(self, sem, mut, nr):
        threading.Thread.__init__(self)
        self.nr = nr
        self.sem = sem
        self.mut = mut

    def run(self):
        while True:
            print(f"Thread {self.nr} acquired mutex")
            with self.mut:
                if random.random() < 0.5:
                    print(f"Thread {self.nr} released semaphore")
                    self.sem.release()

                else:
                    print(f"Thread {self.nr} acquired semaphore")
                    self.sem.acquire()


sem = threading.Semaphore(2)
mut = threading.Semaphore(1)
ths = [MyThread(sem, mut, i) for i in range(10)]

for t in ths:
    t.start()

for t in ths:
    t.join()
