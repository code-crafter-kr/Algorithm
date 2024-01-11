n = int(input())
a = 0

for i in range (n-1, -1, -1):
    print(" "*i, end = "")
    print("*",end="")
    print(" "*a*2, end ="")
    print("*")
    a = a + 1
x = n-1
for j in range (n):
    print(" "*j, end="")
    print("*", end="")
    print(" "*x*2, end="")
    print("*")
    x = x - 1