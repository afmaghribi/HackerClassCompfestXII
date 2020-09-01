#1st step
def pw(masuk):
	panjang = len(str(masuk))//2-1
	hasil = []
	while masuk > 0:
		asli = (masuk >> (panjang << 3))
		geser = (asli << (panjang << 3))
		if asli > 0:
			hasil.append(asli)
		masuk -= geser
		panjang -= 1
	return hasil

#2nd Call
def jj(masuk):
	for i in range(len(masuk)):
		masuk[i] = ((0xF & masuk[i]) << 4) + ((masuk[i] >> 4))
	return masuk

#3rd Call
def hh(masuk):
	for i in range(len(masuk)):
		if (i & 1): # Cek bilangan Ganji
			masuk[i] -= (i + 1) # ganjil masuk sini
		else:
		 	masuk[i] -= (i | 1) # Genap masuk sini
		i += 1
	return masuk

#4th Call
boi = lambda x : ''.join(chr(i) for i in x)

x = input('Flag : ')

flag = pw(int(x))
jj(flag)
hh(flag)
print(boi(flag))
# COMPFEST12{w0W_u_c4n_r3Ad_w3lL}