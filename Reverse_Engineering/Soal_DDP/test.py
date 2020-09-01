#1st Chall
def wg(xy):
	fgx = []
	for i in xy:
		fgx.append(ord(i))
	return fgx # Fungsi mapping list dari tiap char jadi dec

#2nd Call
def hh(xx,yy=0):
	while yy < len(xx):
		if (yy & 1): # Cek bilangan Ganji
			xx[yy] += (yy + 1) # ganjil masuk sini
		else:
		 	xx[yy] += (yy | 1) # Genap masuk sini
		yy += 1
	return xx

#3rd Call
def jj(xx,yy=0):
	for i in range(len(xx)):
		xx[i] = ((0xF & xx[i]) << 4) + ((xx[i] >> 4))
	return xx

#4th Call
def pw(xx, yx=0, xy=0):
	xjl=len(xx)
	while yx < xjl:
		xy = xy + (xx.pop() << (yx << 3))
		yx+=1
	return xy

x = input("Enter an input:")
print(len(x))
gw = wg(x)
print(gw)
print(hh(gw))
print(jj(gw))

yyz = pw(gw)
print(yyz)