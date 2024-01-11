n = int(input())
list_A = [i for i in range (1, n+1)]
a = 0
for i in list_A:
    if i%2 == 0:
        a += i
print(a)