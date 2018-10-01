#!/usr/local/bin/python3

import time
import random
import collections

myd = collections.deque(maxlen = 1000)

def main():
   print('bringing up the rate calculator', current_rate())

   while True:
      r = current_rate()
      print('current rate', str(r))
      rs = random.random()
      time.sleep(rs) # this is proxy for incoming packets
      if rs > 0.99:
         break

   global myd
   print('total elements', str(len(myd)))
   print('time between most recent and least recent', str(myd[-1] - myd[0]))
   print('packet rate', str(len(myd)/(myd[-1] - myd[0])))

def current_rate():
   global myd
   now = time.time()
   myd.append(now)
   sz = len(myd)
   time_span = myd[-1] - myd[0]
   try:
      rate = sz / time_span
   except ZeroDivisionError:
      return 0
   return rate

if __name__ == '__main__':
   main()
