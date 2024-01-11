# 함수 문제 '한수'
N = int(input())

d = 0
if N < 100:
    print(N)
elif N == 1000:
    print("144")
else:
    for i in range ((100), (N+1)):
        i = str(i)
        
        a = int(i[0])
        b = int(i[1])
        c = int(i[2])

        if (a - b == b - c):
            d = d + 1

    print(d + 99)