
N = int(input())
a = "666"
list_A = []

while True:
    if "666" in a:
        list_A.append(a)
        a = str(int(a)+1)
    else:
        a = str(int(a)+1)
    if len(list_A) == N+1:
        break

print(list_A[N-1])