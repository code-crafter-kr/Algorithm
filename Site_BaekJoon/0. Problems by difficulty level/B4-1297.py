a, b, c = map(int, input().split())

a = a ** 2

z = a / (b**2 + c **2)

b = b * (z**0.5)
c = c * (z**0.5)

print(int(b), int(c))