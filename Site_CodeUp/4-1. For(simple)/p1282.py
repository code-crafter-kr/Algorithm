n = int(input())
a = 0
while True:
    if a * a >= n:
        break
    a += 1

if a*a == n:
    print(0, a)
else:
    a -= 1
    print(n-(a*a), a)