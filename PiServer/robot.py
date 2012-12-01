#!/usr/bin/env python

#import os
import time
#import signal
import socket
#from GPIO import * #importing Rasberry Pi GPIO control
from server import * #importing network server class
from move import * #importing the move routines for the robot
 

#Scripting

if __name__ == '__main__':

  #Define attached pin atachments
  Right_R=17
  Right_F=4
  Left_R=21
  Left_F=22

  #setup move routines
  drive=move()
  drive.setup(Right_F,Right_R,Left_F,Left_R)


  #start server
  try:
    soc=server()
    ser=soc.setup(1337,5)
    connection,address = ser.accept()
    while 1:
      message=connection.recv(4096)
      if message == '':
        print "client cut connection, exiting"
        raise KeyboardInterrupt
    
      print message
      if message == 'w':
        drive.forward()
      	time.sleep(.5)
        drive.stop()

      if message == 's':
        drive.reverse()
        time.sleep(.5)
        drive.stop()

      if message == 'a':
        drive.left()
        time.sleep(.5)
        drive.stop()
        
      if message == 'd':
        drive.right()
        time.sleep(.5)
        drive.stop()


  except KeyboardInterrupt:
    print
    print "Cleaning up and exiting" 
    drive.dispatch()
