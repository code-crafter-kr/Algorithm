N = int(input())

list_A = []

for i in range (1, N+1):
    if N % i == 0:
        list_A.append(i)

list_A = list(map(str, list_A))
print(" ".join(list_A))