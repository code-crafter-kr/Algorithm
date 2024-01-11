a = int(input())
x = 1
list_A = [[] for _ in range (a)] 
for ii in range (a):
    if ii % 2 == 1:
        for jj in range (a):
            list_A[jj].append(x)
            x += 1
    else:
        for jj in range (a, 0 ,-1):
            list_A[jj-1].append(x)
            x += 1

for i in list_A:
    print(* i)