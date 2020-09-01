import base36

huruf = base36.dumps(16166842727364078278681384436557013)
flag = ""
for i in huruf:
    flag += chr((ord(i)-97-1-(1^2))%26+97)

print (flag)