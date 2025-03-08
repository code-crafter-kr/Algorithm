import sys
from queue import PriorityQueue #자동으로 추적
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
p = [0] * n # N명의 사람

for i in range (n):
    p[i] = int(input())

pq = PriorityQueue()

for i in range(1, n):
    pq.put(-p[i])

if n == 1:
    print(0)
else:
    count = 0
    while True:
        max_value = -pq.get()
        if max_value < p[0]:
            break
        else:
            max_value -= 1
            p[0] += 1
            count += 1
            pq.put(-max_value)
    print(count)