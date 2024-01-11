a, b = map(float, input().split())
list = []

while a < b + 0.001:
    list.append("%0.2f" %a)
    a = a + 0.01
print(" ".join(list))