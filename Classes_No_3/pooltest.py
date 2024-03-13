from multiprocessing import freeze_support
from multiprocess.pool import Pool, AsyncResult
from time import sleep
from random import random


def f():
    print('Enter')
    sleep(10*random())
    print('Exit')
    return 100


with Pool(processes=2) as pool:
    freeze_support()
    x = pool.apply_async(f, callback=print)
    sleep(100)
    # print(x)
    # print(x.get())
    