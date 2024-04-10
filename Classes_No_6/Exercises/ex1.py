import os
import signal

def child_process():
    while True:
        pass

def main():
    children = []

    # Creating 10 child processes
    for _ in range(10):
        pid = os.fork()
        if pid == 0:  # Child process
            child_process()
        else:
            children.append(pid)

    # Waiting for all child processes to finish
    for pid in children:
        os.waitpid(pid, 0)

    # Killing all processes with one kill command
    os.kill(-os.getpid(), signal.SIGKILL)

if __name__ == "__main__":
    main()
