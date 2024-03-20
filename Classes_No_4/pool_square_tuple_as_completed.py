from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from random import random


def square(i: int) -> int:
    sleep(5*random())
    print(f'Hello {i}')
    sleep(5*random())
    print(f'World {i}')
    return i*i


with ThreadPoolExecutor(max_workers=10) as p:
    it = map(lambda i: p.submit(square, i), range(20))
    print('Waiting .....')
    res = tuple(x.result() for x in as_completed(it))
    print(res)



