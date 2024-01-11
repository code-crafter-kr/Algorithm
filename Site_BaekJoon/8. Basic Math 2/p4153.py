import sys
sys.stdin=open('input.txt','r')

while True:
    list_A = []
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a == 0 and b == 0 and c == 0:
        break

    list_A.append(a)
    list_A.append(b)
    list_A.append(c)
    list_A.sort()

    if list_A[0]**2 + list_A[1]**2 == list_A[2]**2:
        print('right')
    else:
        print("wrong")