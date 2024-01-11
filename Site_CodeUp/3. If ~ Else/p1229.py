a, b = map(float, input().split())

if a>=160:
    x = (a-100)*0.9
    y = (b - x)*100/x

    print("정상" if y <= 10 else "과체중" if y <=20 else "비만")

elif 150 <= a < 160:
    x = (a - 150)/2 + 50
    y = (b - x)*100/x
    print("정상" if y <= 10 else "과체중" if y <=20 else "비만")

else:
    x = a - 100
    y = (b - x)*100/x
    print("정상" if y <= 10 else "과체중" if y <=20 else "비만")