from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import random


def square(i: int) -> int:
    sleep(5*random())
    print(f'Hello {i}')
    sleep(5*random())
    print(f'World {i}')
    return i*i


with ThreadPoolExecutor(max_workers=10) as p:
    it = p.map(square, range(20))
    print('Waiting .....')
    for x in it:
        print(x)

