import numpy as np
hasil = [246, 56, 101, 211, 75, 28, 215, 26, 173, 48, 141, 250, 238, 6, 102, 39, 227, 26, 102, 173, 214, 102, 27, 6, 95, 241, 102, 246, 41, 250, 250, 182]
flag = ""

for i in range(len(hasil)):
	for j in range(130):
		cek = np.float64(j ** 128) % 251
		if cek == hasil[i]:
			print(chr(j),end='')
	print()
# COMPFEST12{tH3_c4T_15_v3rY_Cute}