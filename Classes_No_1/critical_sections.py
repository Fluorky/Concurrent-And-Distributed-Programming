from threading import Thread

counter = 0


def count():
    global counter
    counter = counter + 1


threads = [Thread(target=count) for i in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Threads finished, counter={counter}')
