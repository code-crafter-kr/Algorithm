a, b = map(int, (input().split()))
list_A = [[] for _ in range (a)]
z = 0
y = 1
#제어문을 z로 제어하기

while True:
    if z < a:
        list_A[z].append(y)
        z += 1
        y += 1
