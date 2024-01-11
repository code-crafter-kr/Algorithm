A = int(input())

print("yes" if (A % 4 == 0 and A % 100 != 0) or A%400 == 0 else "no")