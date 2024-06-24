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
            with self.mut:
                print(f"Thread {self.nr} acquired mutex")

                # Symulacja losowej decyzji o użyciu semafora
                if random.random() < 0.5:
                    self.sem.release()
                    print(f"Thread {self.nr} released semaphore")
                else:
                    self.sem.acquire()
                    print(f"Thread {self.nr} acquired semaphore")

                # Symulacja działania
                time.sleep(1)
                print(f"Thread {self.nr} releasing mutex")


sem = threading.Semaphore(2)
mut = threading.Semaphore(1)
ths = [MyThread(sem, mut, i) for i in range(10)]

for t in ths:
    t.start()

for t in ths:
    t.join()
