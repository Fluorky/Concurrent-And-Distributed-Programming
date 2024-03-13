from multiprocessing import freeze_support
from multiprocess.pool import Pool, AsyncResult
from time import sleep
from random import random


def f(x):
    print('Enter')
    sleep(4 * random())
    print('Exit')
    return x * x


with Pool(processes=2) as pool:
    freeze_support()
    x = pool.map_async(f, iterable=range(10), callback=print)
    input('Hello')
    sleep(100)
    # print(x)
    # print(x.get())
