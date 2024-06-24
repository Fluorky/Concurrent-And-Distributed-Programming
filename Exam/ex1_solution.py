import threading
import random
import time

class MyThread(threading.Thread):
    def __init__(self, sem, mut, nr):
        threading.Thread.__init__(self)
        self.nr = nr
        self.sem = sem
        self.mut = mut

    def run(self):
        while True:
            self.sem.acquire()
            print(f"Thread {self.nr} acquired semaphore")

            with self.mut:
                print(f"Thread {self.nr} acquired mutex")

                time.sleep(1)
                print(f"Thread {self.nr} releasing mutex")

            self.sem.release()
            print(f"Thread {self.nr} released semaphore")
            time.sleep(random.random() * 2)


sem = threading.Semaphore(2)
mut = threading.Lock()
ths = [MyThread(sem, mut, i) for i in range(10)]

for t in ths:
    t.start()

for t in ths:
    t.join()
