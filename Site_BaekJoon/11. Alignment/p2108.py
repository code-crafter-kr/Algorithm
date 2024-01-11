import sys
sys.stdin=open('input.txt','r')

n = int(sys.stdin.readline())

list_A = []
for i in range(n):
    list_A.append(int(sys.stdin.readline()))
    
print(round(sum(list_A)/n))

list_A.sort()
print(list_A[int(n//2)])

if len(list_A) == 1:
    print(list_A[0])

else:
    list_X = list_A.copy()

    for i in list_X:
        while True:
            if list_X.count(i) > 1:
                list_X.remove(i)

            if list_X.count(i) == 1:
                break

    list_B = []
    for i in list_X:
        a = list_A.count(i)
        list_B.append([a, i])
    
    list_B.sort()
    list_B.reverse()

    a = list_B[0][0]
    list_C = []
    list_C.append(list_B[0])
    for i in range (1, len(list_B)):
        if list_B[i][0] == a:
            list_C.append(list_B[i])
        else:
            break
        
    if len(list_C) == 2:
        print(list_C[0][1])
    elif len(list_C) == 1:
        print(list_C[0][1])
    else:
        print(list_C[-2][1])


print(max(list_A)-min(list_A))