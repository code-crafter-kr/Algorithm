n = int(input())
x = int(input())
list_A = input().split()
list_A = list(map(int, list_A))
init_n = n
for i in list_A:
    n = n * (1 + i/100)
v = n - init_n 
print("%0.0f" %(v))
print("good" if v >= 0.5 else "bad" if v <= -0.5 else "same")