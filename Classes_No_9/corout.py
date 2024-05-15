def f():
    n = 0
    while True:
        x = yield n
        print(f'Hello: {x}')
        if x == 'exit':
            return

def g(n):
    i = 0
    while i<n:
        yield i
        i = i + 1

x = g(10)
print(x)
print(next(x))