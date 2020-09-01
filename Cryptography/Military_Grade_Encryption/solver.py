def xory(a,b):
	r = ""
	for i,j in zip(a,b):
		r += chr(ord(i) ^ ord(j))
	return r

non = open('not_flag.txt','rb').read()
enc = open('not_flag.enc','rb').read()
flag = open('flag.enc','rb').read()

key = xory(non,enc)
print xory(key,flag)