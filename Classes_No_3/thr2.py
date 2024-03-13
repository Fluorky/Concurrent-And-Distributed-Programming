from threading import Thread
import os
import sys
from time import sleep


def f():
    print('Exitting')
    os.abort()


Thread(target=f).start()
sleep(1)
print('Hello')