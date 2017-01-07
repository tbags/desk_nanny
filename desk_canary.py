#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import serial
import time
import os

def main(argv):
 a = open('status.txt', 'r')
 status = int(a.read(1))
 a.close()
 if(len(argv) == 3):
  ser = serial.Serial('/dev/ttyUSB'+str(argv[2]), 9600)
  count_step = int(argv[1])
  if status+count_step < 12 and argv[0][0] =='u':
   a=open('status.txt', 'w+')
   a.write(str(status+count_step))
  elif status-count_step > 0 and argv[0][0] =='d':
   a=open('status.txt', 'w+')
   a.write(str(status-count_step))
   a.close()
  else:
   return

  for steps in range(0,int(argv[1])):
    ser.write(argv[0][0])
    time.sleep(3)

if __name__ == "__main__":
   main(sys.argv[1:])
