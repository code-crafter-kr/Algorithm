N = input()

for i in N:
    print(chr(ord(i)+2),end = "")
print("")
for i in N:
    print(chr(ord(i)*7%80 + 48), end = "")