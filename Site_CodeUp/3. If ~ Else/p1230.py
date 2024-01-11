list = list(map(int, input().split()))
a = 0
for i in list:
    if i > 170:
        a += 1
    elif i <= 170:
        print("CRASH", i)
        break

if a == 3:
    print("PASS")
