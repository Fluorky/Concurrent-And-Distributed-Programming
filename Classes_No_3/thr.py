from threading import Thread
import os
import sys
from time import sleep


def f():
    print('Exitting')
    os._exit(1)


Thread(target=f).start()
sleep(1)
print('Hello')