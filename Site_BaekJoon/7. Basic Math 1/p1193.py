# 등차수열로 특정 N이 주어질 때 특정 숫자 a열 구하는 함수.
N = int(input())
n = 1
B = N
list_N = []

if N == 1:
    print("1/1")

else:
    while True:
        B = B - n
        n = n + 1
        if B <= 0:
            N = B + n
            break
        a = n
        
    for i in range (1, a+1):
        d = "{0}/{1}".format(i, a)
        a = a - 1
        list_N.append(d)
        
    if n % 2 != 0:
        print(list_N[N-2])

    if n % 2 ==0:
        list_N.reverse()
        print(list_N[N-2])