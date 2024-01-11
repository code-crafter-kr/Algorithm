#기본수학 1 '설탕 배달'
list_A = [3, 6, 9, 12]
N = int(input())
for i in list_A:
    if N == i:
        print(N // 3)
        break

if N % 5 == 0:
    print(N//5)
elif not N in list_A:
    for i in range (1, 1666):
        A = N - i*3
        if A <= 0:
            print("-1")
            break
        elif A % 5 == 0:
            print(A//5 + i)
            break