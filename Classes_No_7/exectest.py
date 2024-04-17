from os import execl

print('Before execl')
try:
    execl('/bin/ls', 'ls', '-l')
except FileNotFoundError:
    print("After execl")
