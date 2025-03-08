import sys
from queue import PriorityQueue
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M, X = map(int, input().split()) # N명의 학생, M개의 도로, X마을

adj = [[] for i in range (N)]
for i in range (M):
    start, end, distance = map(int, input().split())
    adj[start-1].append((end-1, distance))

pq = PriorityQueue()
ans = [1e9] * N
X = X - 1
# 돌아오는길의 출발지는 모두 같으므로 그거부터 계산
pq.put((0, X))
ans[X] = 0
while pq.qsize() != 0:
    distance, node = pq.get()
    if distance > ans[node]:
        continue

    for v, w in adj[node]:
        if ans[v] > ans[node] + w:
            ans[v] = ans[node] + w
            pq.put((ans[v], v))
print(ans)
# 가는길 계산해서 맞는 인덱스에 모두 추가
for i in range (N):
    pq = PriorityQueue()
    dist = [1e9] * N
    dist[i] = 0
    pq.put((0, i))
    while pq.qsize() != 0:
        distance, node = pq.get()
        if distance > dist[node]:
            continue

        for v, w in adj[node]:
            if dist[v] > dist[node] + w:
                dist[v] = dist[node] + w
                pq.put((dist[v], v))
    print(i, dist)
    ans[i] += dist[X]
print(ans)
print(max(ans))


