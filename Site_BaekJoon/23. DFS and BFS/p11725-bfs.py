import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(n):
    Q = deque()
    Q.append(1) #첫 노드는 무조건 1이니깐.

    while Q:
        n = Q.popleft()
        visited[n] = 1 # 바로 방문처리

        for x in graph[n]: #방문한 노드의 요소들 뽑아내기 방문한 노드면 뽑아낼 필요 x
            if visited[x] == 1:
                pass

            else:
                Q.append(x)
                ans[x] = n # x번 노드의 엄마는 n이 된다.

n = int(sys.stdin.readline())
visited = [0] * (n+1)
ans = [[] for _ in range (n+1)]
graph = [[] for _ in range (n+1)]

for _ in range (n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) 

bfs(1) #1번 노드부터 체크
for i in range (2, n + 1): #2번 노드부터 확인한다
    print(ans[i])