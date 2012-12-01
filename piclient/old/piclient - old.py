#!/usr/bin/env python
## piclient.py

import socket
import time
import tty
import sys
import termios


HOST = '192.168.3.100' #pi address
PORT = 1337
ADDR = (HOST,PORT)
BUFSIZE = 4096

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect((ADDR))

#Setup the terminal
#Save old settings
fd=sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
  tty.setraw(sys.stdin.fileno())
  while 1:
    message=sys.stdin.read(1)
    
    if message == 'q':
      termios.tcsetattr(fd,termios.TCSADRAIN, old_setings)
      client.close()
    #message=raw_input()
    client.send(message)
finally:
  termios.tcsetattr(fd,termios.TCSADRAIN, old_setings)
  client.close()
