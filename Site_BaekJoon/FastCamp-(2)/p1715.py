import sys
from queue import PriorityQueue
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


pq = PriorityQueue()
n = int(input())

for i in range(n):
    num = int(input())
    pq.put(num)

result = 0
if n == 0:
    print(0, end = "")
else:    
    while True:
        if pq.qsize() == 1:
            print(result, end = "")
            break
        else:
            a1 = pq.get()
            a2 = pq.get()
            temp = a1 + a2
            pq.put(temp)
            result += temp