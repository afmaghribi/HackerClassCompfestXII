import os

flag = open('flag.txt').read()

ekwk = bin(int(flag.encode('hex'), 16)).strip('0b')

# print ekwk

for i in range(len(ekwk)):
    if ekwk[i] == '1':
        os.system('cp batman.png {}.png'.format(i))
    elif ekwk[i] == '0':
        os.system('cp nightwing.png {}.png'.format(i))

os.system('rm flag.txt')
