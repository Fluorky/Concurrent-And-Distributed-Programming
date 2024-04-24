import os
import random
import sys


def child(pipe_in, pipe_out):
    while True:
        received = pipe_in.readline().strip()
        if not received:
            break
        number = float(received)
        square = number ** 2
        pipe_out.write(f"{square}\n")
        pipe_out.flush()


def parent(pipe_in, pipe_out):
    n = random.randint(0, 200)
    for _ in range(n):
        number = 10 * random.random()
        pipe_out.write(f"{number}\n")
        pipe_out.flush()
        received = pipe_in.readline().strip()
        print(f"Sent: {number}, Received: {received}")


if __name__ == "__main__":
    pipe_cin, pipe_cout = os.pipe()
    pipe_pin, pipe_pout = os.pipe()

    pid = os.fork()

    if pid == 0:
        # Child process
        os.close(pipe_cout)
        os.close(pipe_pin)
        child_pipe_in = os.fdopen(pipe_cin, 'r')
        child_pipe_out = os.fdopen(pipe_pout, 'w')
        child(child_pipe_in, child_pipe_out)
        child_pipe_in.close()
        child_pipe_out.close()
        sys.exit(0)
    else:
        # Parent process
        os.close(pipe_cin)
        os.close(pipe_pout)
        parent_pipe_in = os.fdopen(pipe_pin, 'r')
        parent_pipe_out = os.fdopen(pipe_cout, 'w')
        parent(parent_pipe_in, parent_pipe_out)
        parent_pipe_in.close()
        parent_pipe_out.close()
        os.waitpid(pid, 0)
