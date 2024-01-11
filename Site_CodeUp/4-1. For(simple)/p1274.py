N = int(input())

list_A = []

for i in range (1, N+1):
    if N % i == 0:
        list_A.append(i)

if len(list_A) == 2:
    print("prime")
else:
    print("not prime")