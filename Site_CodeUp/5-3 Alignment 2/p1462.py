n = int(input())
list_A = []
z = 1
y = 0
for i in range(n):
    y = 0
    for j in range(n):
        list_A.append(z + y*n)
        y = y + 1
    z = z + 1
    print(* list_A)
    list_A= []