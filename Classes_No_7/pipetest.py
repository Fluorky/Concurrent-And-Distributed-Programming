import os

# The parent process sends a text message through a pipe
# to the child process, which prints this message on the console

# r - read end of the pipe
# w - write end of the pipe
r, w = os.pipe()

if os.fork() > 0:
    # Parent process code
    # Parent closes the unnecessary read end of the pipe
    os.close(r)
    # Parent wraps the write end of the pipe with a stream
    w = os.fdopen(w, "w")
    # Parent sends the message to the child
    w.write("Hello World\n")
    # Parent closes the output stream
    w.close()
    # Parent waits for the child to finish
    os.wait()
else:
    # Child process code
    # Child closes the unnecessary write end of the pipe
    os.close(w)
    # Child wraps the read end of the pipe with a stream
    r = os.fdopen(r, "r")
    # Child reads
    msg = r.read()
    print('Received:', msg)
    # Child closes the read end of the pipe
    r.close()
