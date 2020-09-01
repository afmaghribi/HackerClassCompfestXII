from z3 import *
import numpy as np
import math

hasil = [246, 56, 101, 211, 75, 28, 215, 26, 173, 48, 141, 250, 238, 6, 102, 39, 227, 26, 102, 173, 214, 102, 27, 6, 95, 241, 102, 246, 41, 250, 250, 182]
ch = [z3.Real('k_{}'.format(x)) for x in range(32)]

s = Solver()
for i in range(32):
	s.add((ch[i]**128) % 251 == hasil[i])


if solver.check():
	results = solver.model()
	for character in password:
		flag = flag + chr(results[character].as_long())
	else:
		print(flag)