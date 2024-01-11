a = int(input())
list = []

for i in range (1, a+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        list.append("X")
    else:
        list.append("%d" %i)

print(" ".join(list))