from os import fork, wait, getpid
from time import sleep
from sys import argv


def chain(n: int):
    for _ in range(n - 1):
        child = fork()
        pid = getpid()
        if child > 0:
            print(f'Parent, pid = {pid}, child pid = {child}')
            wait()
            print(f'Child pid={child} finished')
            return
        print(f'Child, pid={pid}')

    while True:
        sleep(1)


def tree(n: int):
    for i in range(n):
        child = fork()
        pid = getpid()
        if child == 0:
            print(f'Child, pid={pid}')
            while True:
                sleep(1)
        print(f'Parent, pid = {pid}, child pid = {child}')

    for i in range(n):
        print(f'Waiting for {i}''th child')
        wait()


n = int(argv[2])
if argv[1] == 'chain':
    chain(n)
else:
    tree(n)