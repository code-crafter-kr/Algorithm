import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


M, N = map(int, input().split())
visited = [0] * (M+1)
adj = [[] for _ in range (M+1)]
for i in range (N): 
    a, b = map(int, input().split())
    adj[a].append(b) # 어디노드가 어디로 이어지는지 (숫자가 인덱스 이어지는길이 직접적으로 이어짐)
    adj[b].append(a)

count = 0 


for i in range(1, N+1):
    if visited[i] == 1:
        continue
    count += 1

    que = deque([i])
    visited[i] = 1
    while len(que) != 0:
        u = que.popleft()

        for j in adj[u]:
            if visited[j] == 0:
                que.append(j)
                visited[j] = 1

print(count)