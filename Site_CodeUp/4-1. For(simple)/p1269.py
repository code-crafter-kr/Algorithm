a, b, c, d = map(int, input().split())
if d == 1:
    print(a)

for i in range(1, d):
    a = a * b + c

print(a)