from z3 import *

ans = [0x00000092,0x000014ad,0x0000009d,0x00001810,0x0000008b,0x000012de,0x000000a7,0x00001b3c,0x00000063,0x00000992,0x000000dd,0x00002f16,0x000000d3,0x00002b66,0x000000d3,0x00002b32,0x000000ca,0x000027b5,0x000000cf,0x000029ae,0x000000cd,0x000028d2,0x000000ce,0x00002931,0x000000d7,0x00002d1e,0x000000cf,0x000029d2,0x000000d7,0x00002cdc,0x000000c8,0x000026f7,0x000000d8,0x00002d8c,0x000000c8,0x0000270f,0x000000d3,0x00002b0c,0x000000db,0x00002ed4,0x000000e9,0x000034bc]

password = [BitVec('x{}'.format(x), 32) for x in range(42)]

s = Solver()
for i in range(len(password)): #printable range 0x20 - 0x7f atau (32-127)
  s.add(password[i] >= 32)
  s.add(password[i] < 127)

for j in range(0,len(password),2):
	s.add(password[j]*password[j + 1] == ans[j + 1])
	s.add(password[j]+password[j + 1] == ans[j])

if s.check() == z3.sat:
    model = s.model()
    solution = ''.join([chr(int(str(model[password[i]]))) for i in range(42)])
    print solution
# COMPFEST12{benar_kan_no_inject_inject_lol}