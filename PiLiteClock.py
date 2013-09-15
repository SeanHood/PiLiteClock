#!/usr/bin/python

import math, datetime, sys
from pprint import pprint
import random

lst = []

hr = range(2,14)
am = range(1,5)
pm = range(6,10)

for h in hr:
	for m in am:
		lst.append(str(h) + ',' + str(m))

for h in hr:
	for m in pm:
		lst.append(str(h) + ',' + str(m))

t = datetime.datetime.now()
h = t.hour * 4
m = math.ceil(float(t.minute) / 15)
c = int(h + m - 1)

def output():
	import serial
	s = serial.Serial()
	s.baudrate = 9600
	s.timeout = 0
	s.port = "/dev/ttyAMA0"
	
	try:
		s.open()
	except serial.SerialException, e:
		sys.stderr.write("Could not open port %r: %s\n" % (port,e))
		sys.exit(1)
		
	s.write("$$$ALL,OFF\r")

	pix = range(c)
	random.shuffle(pix)
	
	for p in pix:
		s.write("$$$P" + lst[p] + ",ON\r")


## Lets Run
output()

sys.exit()
