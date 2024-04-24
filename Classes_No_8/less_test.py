# Now I don't need to add the os. prefix to these functions
from os import pipe, fork, dup2, execl, close, fdopen, wait

r, w = pipe()

if fork() > 0:
    # Always remember to close unnecessary pipe ends
    close(r)
    with fdopen(w, 'w') as w:
        for i in range(100):
            for j in range(100):
                k = i * j
                print(f'{i:3}×{j:3} = {k:5}', file=w)
    wait()
else:
    # Always remember to close unnecessary pipe ends
    close(w)
    # Copy r to the child's standard input
    dup2(r, 0)
    # Execute less
    execl('/usr/bin/less', 'less')
    # Now the standard input for less is connected to
    # the reading end of the pipe
