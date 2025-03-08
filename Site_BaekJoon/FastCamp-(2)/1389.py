import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M = map(int, input().split())

adj = [[] for _ in range (N)]
for i in range (M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1) # 넘버 다 한칸씩 당기기

minimum = 1000000

for i in range (N): #사람 수 만큼 체크
    visited = [0] * N
    que = deque([i]) # 시작점
    visited[i] = 1

    while que:
        next_vistid = que.popleft()
        for j in adj[next_vistid]:
            if visited[j] != 0:
                continue
            else:
                visited[j] = visited[next_vistid] + 1
                que.append(j)
    
    if sum(visited) < minimum:
        minimum = sum(visited)
        result = i

print(result+1)