from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from random import random


def multiply_table(entry: tuple) -> tuple:
    num1, num2 = entry
    sleep(1*random())
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
    return num1, num2, result


with ThreadPoolExecutor(max_workers=10) as p:
    entries = ((i, j) for i in range(1, 11) for j in range(1, 11))
    it = map(lambda entry: p.submit(multiply_table, entry), entries)
    print('Waiting .....')
    multiplication_dict = {}
    for future in as_completed(it):
        number1, number2, res = future.result()
        multiplication_dict[(number1, number2)] = res
    print('Multiplication results:', multiplication_dict)
