A = list(map(int, input().split()))
list_A = [i for i in range (A[0], A[1]+1)]

for i in list_A:
    for jj in range (1, 10):
        print("%d*%d=%d" %(i, jj, i*jj))