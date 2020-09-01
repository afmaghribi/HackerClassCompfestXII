from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.number import *

aes = AES.new('supersecretvalue', AES.MODE_ECB)

r = remote('128.199.104.41', 25300)
flag = ''

for i in range(1,11):
	r.sendlineafter('Please select a lab member (or 0 to break): ',str(i))
	r.recvuntil('0.')
	cipher = r.recvuntil('\n',drop=True).strip()
	flag += aes.decrypt(long_to_bytes(int(cipher)))


print(flag)