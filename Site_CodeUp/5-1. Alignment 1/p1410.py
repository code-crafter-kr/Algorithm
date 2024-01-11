n = input()
a = 0
b = 0
for i in n:
    if i == "(":
        a = a + 1
    else:
        b = b + 1

print(a,b)