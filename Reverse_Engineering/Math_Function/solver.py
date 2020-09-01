from z3 import *

solver = Solver()

password = [ z3.Int("password_{}".format(num)) for num in range(4) ]

solver.add(
	(password[0] * 50) +
	(password[1] * 11) +
	(password[2] * 18) +
	(password[3] * 12) == 7681
)
solver.add(
	(password[0] * 18) +
	(password[1] * 12) +
	(password[2] * 23) +
	(password[3] * 2 ) == 4019
)
solver.add(
	(password[0] * 21) +
	(password[1] * 11) +
	(password[2] * 35) +
	(password[3] * 42) == 7160
)
solver.add(
	(password[0] * 47) +
	(password[1] * 2 ) +
	(password[2] * 12) +
	(password[3] * 40) == 8080
)

flag = ""

if solver.check():
	results = solver.model()
	for character in password:
		flag = flag + chr(results[character].as_long())
	else:
		print(flag)

import numpy as np
import hashlib

data = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])
my_input = flag
password = np.array(list(map(ord, list(my_input[:4].ljust(4, '\x00')))))
print(password)
result = list(np.matmul(data, password))
print(result)
if result == [7681, 4019, 7160, 8080]:
	print("Congratz, here is your flag: COMPFEST12{" + hashlib.sha384(bytes(my_input.encode())).hexdigest() + "}")
