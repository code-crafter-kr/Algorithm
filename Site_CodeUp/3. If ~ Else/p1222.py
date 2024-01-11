a,b,c = map(int, input().split())

a = ((89 - a) // 5) + 1

print("same" if a + b == c else "win" if a+b > c else "lose" )