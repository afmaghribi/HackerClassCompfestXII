from z3 import *

passwd = [Int("password_{}".format(num)) for num in range(4)]

s = Solver()
a = [[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]]
h = [7681, 4019, 7160, 8080]

for i in range(4):
	s.add((passwd[0]*a[i][0]) + (passwd[1]*a[i][1]) + (passwd[2]*a[i][2]) + (passwd[3]*a[i][3]) == h[i])

flag = ""

if s.check():
	results = s.model()
	for character in passwd:
		flag = flag + chr(results[character].as_long())
	else:
		print(flag)

import numpy as np
import hashlib

data = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])
my_input = flag
password = np.array(list(map(ord, list(my_input[:4].ljust(4, '\x00')))))
result = list(np.matmul(data, password))
print(result)
if result == [7681, 4019, 7160, 8080]:
	print("Congratz, here is your flag: COMPFEST12{" + hashlib.sha384(bytes(my_input.encode())).hexdigest() + "}")
