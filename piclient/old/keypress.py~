#!/usr/bin/env python
import termios, fcntl, sys, os
import socket
import time
#setup network client
HOST = '192.168.3.100' #pi address
PORT = 1337
ADDR = (HOST,PORT)
BUFSIZE = 4096
client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect((ADDR))


#Setup Terminal
fd = sys.stdin.fileno()
oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            print "Got character", repr(c)
            client.send(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    client.close()