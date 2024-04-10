import os

def child_process():
    while True:
        pass

def main():
    # Creating a chain of 11 processes
    for _ in range(10):
        pid = os.fork()
        if pid == 0:  # Child process
            child_process()
            os._exit(0)  # Exiting the child process after finishing the loop
        else:
            os.waitpid(pid, 0)  # Parent process waits for the child to finish

    # The last process enters an infinite loop
    child_process()

if __name__ == "__main__":
    main()
