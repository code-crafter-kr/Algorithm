a = 0
b = 0
c = int(input())
while True:
    a += 1
    b += a
    if b >= c:
        break
print(b)