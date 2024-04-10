import os

print('Hello before fork')
try:
    pid = os.fork()
    if pid > 0:
        print("I am a parent process, my child's pid =", pid,
              ", my pid = ", os.getpid())
    elif pid == 0:
        print("I am a child process, my pid =", os.getpid(),
              "my parent's pid =", os.getppid())
    else:
        print("Impossible return value, your computer is posessed by demons")
except OSError as err:
    print("fork() failed, your system is seriously messed up, reboot and hope for the best")
    print("Details:", inst)