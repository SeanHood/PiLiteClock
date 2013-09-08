#!/usr/bin/python

# PiLiteClock
# Copyright (C) 2013 Sean Hood
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# https://github.com/seanhood/PiLiteClock

import math, datetime, sys

lst = []

h = 1
while h < 13:
	h = h + 1	
	m = 1
	while m < 5:
		lst.append(str(h) + ',' + str(m))
		m = m +1 
h = 1
while h < 13:
	h = h + 1	
	m = 6
	while m < 10:
		lst.append(str(h) + ',' + str(m))
		m = m +1	

t = datetime.datetime.now()
h = t.hour * 4
m = math.ceil(float(t.minute) / 15)
c = int(h + m)

def output(x):
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
	
	for i in range(c):
		s.write("$$$P" + lst[i] + ",ON\r")	

## Lets Run
output(c)

sys.exit()
