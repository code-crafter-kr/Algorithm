a = input()
a = (a[1] + a[0] if int(a)>=10 else int(a)*10)
print(int(a)*2 if int(a)*2 <100 else (int(a)*2%100), "\nGOOD" if int(a)*2%100 <= 50 else "\nOH MY GOD")