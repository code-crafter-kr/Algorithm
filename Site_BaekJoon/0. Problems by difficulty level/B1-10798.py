import sys
sys.stdin = open("input.txt", "r")

x, y = 5, 0 
lst = []
for i in range (5):
    temp = input()
    y = max(len(temp), y)
    lst.append(temp)


for j in range (y):
    for i in range (x):
        try:
            print(lst[i][j], end = "")
        except:
            pass
