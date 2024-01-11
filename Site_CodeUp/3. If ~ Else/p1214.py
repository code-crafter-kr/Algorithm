A, B = map(int, input().split())

if B == 2:
    if A % 4 == 0 and A % 100 != 0 or A%400 == 0:
        print(29)
    else:
        print(28)

elif B in [1,3,5,7,8,10,12]:
    print("31")

else:
    print("30")