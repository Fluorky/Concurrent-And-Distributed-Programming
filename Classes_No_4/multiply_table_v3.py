from concurrent.futures import ThreadPoolExecutor, as_completed


def mult(i, j):
    return i * j


with ThreadPoolExecutor(max_workers=10) as p:
    it = [(i, j, p.submit(mult, i, j)) for i in range(11) for j in range(11)]
    res = {(i, j): fut.result() for i, j, fut in it}
    print(res)
