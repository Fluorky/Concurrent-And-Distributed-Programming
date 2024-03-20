from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import random


def f():
    sleep(5*random())
    print('Hello')
    sleep(5*random())
    print('World')
    return 42


with ThreadPoolExecutor(max_workers=10) as p:
    res = p.submit(f)
print('Waiting....')
print(res.result())
