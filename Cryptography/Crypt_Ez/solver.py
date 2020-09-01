import random as ciwi

p = 101 #
q = 211 # Dari factordb.com 21311
n = 21311 # hint: n = p*q

enc = open('enc','r').read()

form = "COMPFEST12{budayakan_jujur_dan_tamvan_007_12aba}"

ciwi.seed(q)

enc2 = ""
for i in range(10, len(enc) + 10):
    i -= 1
    z = p + q - i
    enc2 += chr(ord(enc[i - 9]) ^ ciwi.randint(i, z))

print(enc2)

ciwi.seed()

enc = ""
for i in range(len(enc2)):
	if i < len(form):
		for j in range(1,5):
			tmp = chr((ord(enc2[i]) - j)//5)
			if (tmp == form[i]):
				enc += tmp
				break
	else:
		enc += chr((ord(enc2[i]) - ciwi.randint(1,4))//5)

print (enc)