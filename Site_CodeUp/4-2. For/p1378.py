n = int(input())
a = 0
for i in range (n+1):
    for j in range (i+1):
        a = a + j
print(a)