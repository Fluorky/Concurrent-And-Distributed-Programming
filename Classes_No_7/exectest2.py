from os import execl

print('Before execl')
try:
    execl('/bin/ls2', 'ls', '-l')
except FileNotFoundError:
    print("After execl")
