#브루트 포스 문제 '분해합'
N = int(input())
c = 0
for B in range (int(N/2), N):
    B = str(B)
    A = 0
    for i in B:
        A = int(i) + A
    A = A + int(B)

    if A == N:
        print(B)
        c = 1
        break

if c == 0:
    print(0)