#!/usr/bin/env python
## piclient.py

import socket
import time

#imports for terminal key capture
import termios, fcntl, sys, os



HOST = '192.168.3.100' #pi address
PORT = 1337
ADDR = (HOST,PORT)
BUFSIZE = 4096

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect((ADDR))

#Setup the terminal
#Save old settings
fd=sys.stdin.fileno()
oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3]=newatr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd,termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
  while 1:
    message=sys.stdin.read(1)
    client.send(message)
finally:
  #termios.tcsetattr(fd,termios.TCSADRAIN, old_setings)
  termios.tcsetattr(fd,termios.TCSAFLUSH, oldterm)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
  client.close()
