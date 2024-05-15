def culler(p: int):
    next_proc = None
    n = p
    ret = (n, True)
    while True:
        n = yield ret
        if n % p == 0:
            ret = (n, False)
        else:
            if next_proc:
                ret = next_proc.send(n)
            else:
                next_proc = culler(n)
                ret = next(next_proc)


pipe = culler(2)
print(next(pipe))
for n in range(3, 100):
    print(pipe.send(n))
