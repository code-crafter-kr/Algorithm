n = int(input())
z = 1
list_A = []
for i in range(n):
    for j in range(n):
        list_A.append(z)
        z = z + 1
    list_A.reverse()
    print(* list_A)
    list_A= []