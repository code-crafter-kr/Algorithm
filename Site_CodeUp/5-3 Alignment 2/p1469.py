a = int(input())

for i in range (a):
    list_A = []
    for j in range (a):
        list_A.append(j+1 + a*i)
    if i % 2 == 1:
        print(* list_A)
    else:
        list_A.reverse()
        print(* list_A)

