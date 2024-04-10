import os, time

if os.fork() > 0:
    print('parent, pid =', os.getpid())
    print('Entering infinite loop...')
    while True:
        time.sleep(1)
else:
    print('Child, pid =', os.getpid())