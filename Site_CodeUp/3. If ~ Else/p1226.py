list_A = input().split()
list_B = input().split()
a = 0
for i in list_B:
    if i in list_A[:6]:
        a += 1

if a == 5 and list_A[-1] in list_B:
    print(2)
else:
    print("1" if a == 6 else "3" if a == 5 else "4" if a == 4 else "5" if a == 3 else "0")