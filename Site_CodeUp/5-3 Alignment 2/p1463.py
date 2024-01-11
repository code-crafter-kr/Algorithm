n = int(input())
list_A = []
for i in range (n, 0, -1):
    for j in range (n):
        list_A.append(i + j*n)
    print(* list_A)
    list_A = []
