a, b = map(int, input().split())
c = a * b - a + 1
z = 0
for ii in range (a):
    list_A = []
    for jj in range (b):
        list_A.append(c - z*a)
        z += 1
    c = c + 1
    z = 0
    print(* list_A)