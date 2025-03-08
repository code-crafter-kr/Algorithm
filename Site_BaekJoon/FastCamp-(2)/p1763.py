import sys
from queue import PriorityQueue
input = sys.stdin.readline



V, E = map(int, input().split()) # Verticles, edges 
K = int(input()) - 1 # 0번부터 시작
adj = [[] for i in range (V)]

for i in range (E):
    u, v, w = map(int, input().split())
    adj[u-1].append((v-1, w))

dist = [1e9] * V
pq = PriorityQueue()

dist[K] = 0
pq.put((0, K)) #시작점을 일단 푸쉬

while pq.qsize() != 0:
    distance, node = pq.get()

    if distance > dist[node]:
        continue
    
    for v, w in adj[node]:
        if dist[v] > dist[node] + w:
            dist[v] = dist[node] + w
            pq.put((dist[v], v))

for i in range (V):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])