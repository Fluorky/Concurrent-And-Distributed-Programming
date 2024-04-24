import os, sys

# sys.argv[0] will contain the script name.
path = sys.argv[0]
# The os.open() function, unlike open(),
# returns a file descriptor instead of a file object.
# os.O_RDONLY is a flag indicating that the file
# is being opened for reading only.
fd = os.open(path, os.O_RDONLY)
# Copy the file descriptor fd to standard input.
os.dup2(fd, 0)
# Execute cat within the current process.
os.execl('/bin/cat', 'cat')
# The standard input for cat is now the same as fd,
# i.e., the opened file descriptor to this script file.
