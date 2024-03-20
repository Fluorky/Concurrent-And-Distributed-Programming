from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from random import random


def multiply_table(entry: tuple) -> int:
    num1, num2 = entry
    sleep(1*random())
    print(f'{num1} * {num2} = {num1*num2}')
    return num1*num2


with ThreadPoolExecutor(max_workers=10) as p:
    entries = ((i, j) for i in range(1, 11) for j in range(1, 11))
    it = map(lambda entry: p.submit(multiply_table, entry), entries)
    print('Waiting .....')
    res = tuple(x.result() for x in as_completed(it))
    print('Multiplication results:', res)
