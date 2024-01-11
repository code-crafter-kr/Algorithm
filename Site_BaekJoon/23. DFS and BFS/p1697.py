import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
Q = deque()
Q.append(N)

visited = [0] * 100001

if N == K:
    print(0)

else:
    while Q:
        x = Q.popleft()

        if x == K:
            print(visited[x])
            break

        for nx in [x+1, x-1, x*2]:
            if 0 <= nx <= 100000 and visited[nx] == 0: # 가본적이 없으면 첫방문.
                visited[nx] = visited[x] + 1 # 거쳐올라간 횟수 (이전의 횟수 + 1) 세대를 거듭한다고 보면 될듯.
                Q.append(nx)