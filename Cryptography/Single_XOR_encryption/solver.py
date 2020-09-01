cipher = open('soal','r').read().decode('hex')

for i in range(256):
	flag = ""
	for j in cipher:
		flag += chr(ord(j) ^ i)
	print flag,i