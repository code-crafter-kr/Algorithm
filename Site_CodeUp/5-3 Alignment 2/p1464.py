a, b = map(int, input().split())
c = a*b
for ii in range(a):
    list_A = []
    for jj in range(b):
        list_A.append(c)
        c -= 1
    print(* list_A)
