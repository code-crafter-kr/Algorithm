n, x = map(int,input().split())
print("+",end ="")
print("-"*(n-2),end ="")
print("+")

for i in range (x-2):
    print("|",end ="")
    print(" "*(n-2), end="")
    print("|")

print("+",end ="")
print("-"*(n-2),end ="")
print("+")