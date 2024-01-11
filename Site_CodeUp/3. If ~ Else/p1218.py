a, b, c = map(int,input().split())
list = [a,b,c]
list.sort()

if c >= a + b:
    print("삼각형아님")
elif list[0] == list[2]:
    print("정삼각형")
elif list[2]**2 == list[0]**2 + list[1]**2:
    print("직각삼각형")
elif list[0] == list[1] or list[1] == list[2]:
    print("이등변삼각형")
else:
    print("삼각형")