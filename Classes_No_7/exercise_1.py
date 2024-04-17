import os
import random


def parent_to_child(pipe_parent_to_child):
    # Close the read end of the pipe
    pipe_parent_to_child[0].close()

    n = random.randint(0, 200)
    for _ in range(n):
        num = str(random.randint(0, 10))
        pipe_parent_to_child[1].write(num.encode() + b'\n')
        pipe_parent_to_child[1].flush()
        response = pipe_parent_to_child[1].readline().decode().strip()
        print(f"Parent sent: {num}, Child responded: {response}")

    # Close the write end of the pipe
    pipe_parent_to_child[1].close()


def child_to_parent(pipe_parent_to_child):
    # Close the write end of the pipe
    pipe_parent_to_child[1].close()

    for line in pipe_parent_to_child[0]:
        num = float(line.decode().strip())
        square = num ** 2
        pipe_parent_to_child[0].write(f"{square}\n".encode())
        pipe_parent_to_child[0].flush()

    # Close the read end of the pipe
    pipe_parent_to_child[0].close()


def main():
    # Create a pipe
    pipe_parent_to_child = os.pipe()

    pid = os.fork()

    if pid > 0:
        # Parent process
        parent_to_child(pipe_parent_to_child)
        os.wait()
    elif pid == 0:
        # Child process
        child_to_parent(pipe_parent_to_child)
        os._exit(0)
    else:
        print("Fork failed")


if __name__ == "__main__":
    main()
