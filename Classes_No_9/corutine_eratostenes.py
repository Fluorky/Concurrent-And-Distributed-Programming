# Eratosthenes' sieve written using coroutines, takes and checks a number, adds it to the next coroutines if it's
# a valid prime.

def sieve():
    primes = []
    while True:
        num = yield
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            print(f"Prime found: {num}")


def main():
    s = sieve()
    next(s)  # Start the coroutine
    for i in range(2, 10000):
        s.send(i)


if __name__ == "__main__":
    main()
