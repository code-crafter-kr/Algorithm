import sys
input = sys.stdin.readline

def my_round(x):
    return int(x + 0.5)

n = int(input())

start = my_round(n * (15 / 100))
end = n - start

if n == 0:
    print(0)

else:
    lst = []
    for i in range(n):
        lst.append(int(input()))

    lst.sort()
    print(my_round(sum(lst[start:end]) / (n - start * 2)))