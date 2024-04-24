import os
import time

def create_child():
    pid = os.fork()
    if pid == 0:
        print("Child process with PID:", os.getpid())
        time.sleep(1)
        exit(0)
    else:
        os.waitpid(pid, 0)


def main():
    print("Parent process with PID:", os.getpid())
    for _ in range(10):
        create_child()
    while True:
        pass


if __name__ == "__main__":
    main()
