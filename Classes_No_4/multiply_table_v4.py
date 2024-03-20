from concurrent.futures import ThreadPoolExecutor, as_completed


def mult(i, j):
    return i, j, i * j


with ThreadPoolExecutor(max_workers=10) as p:
    it = [p.submit(mult, i, j) for i in range(10) for j in range(10)]
    res = {(i, j): result for i, j, result in (future.result() for future in as_completed(it))}
    print(res)
