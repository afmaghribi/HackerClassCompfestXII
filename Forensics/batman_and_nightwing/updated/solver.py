import os
from Crypto.Util.number import *

flag = ''

for i in range(359):
	cek = os.system('diff {}.png batman.png'.format(i))
	if cek:
		flag += '0'
	else:
		flag += '1'

flag = long_to_bytes(int(flag,2)).decode()

print (flag)