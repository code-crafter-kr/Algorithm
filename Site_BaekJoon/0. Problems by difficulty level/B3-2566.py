import sys
sys.stdin = open("input.txt", "r")

maximum, x, y = -1, -1, -1

for i in range (9):
    temp = list(map(int, input().split()))
    maximum = max(maximum, max(temp))
    if maximum in temp:
        x = i + 1 
        y = temp.index(maximum) +1

print(maximum)
print(x, y)