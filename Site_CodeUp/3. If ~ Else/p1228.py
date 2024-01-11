a, b = map(float, input().split())

x = (a-100)*0.9
y = (b - x)*100/x

print("정상" if y <= 10 else "과체중" if y <=20 else "비만")