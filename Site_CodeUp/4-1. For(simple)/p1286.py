list_A = []
for i in range (5):
    list_A.append(int(input()))

min = -1000000
max = 1000000
for i in list_A:
    if max >= i:
        max = i
    if min <= i:
        min = i

print(min)
print(max)
    