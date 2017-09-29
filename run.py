"""
run.py
"""

from fizz_rnd_list import Fizz_Rnd_List
import numpy as np
import sys


if len(sys.argv) != 2:
	raise ValueError('Wrong number of arguments; please provide an integer greater than 0')
try:
	n = int(sys.argv[1])
	assert n >= 0
except:
	raise ValueError('Please provide a valid integer greater than 0')

fizz = Fizz_Rnd_List(n)
for i in range(n):
	x = np.random.uniform(0.0, 1.0)
	y, m, mean, std_dev = fizz.get_stats(x)
	print("ITERATION:", i)
	#print("the list:", fizz.lst)  #extra prints for more info
	#print("inputed x:", x)
	print("y =", y)
	print("m =", m)
	print("mean =", mean)
	print("std_dev =", std_dev)
	print("\n")
