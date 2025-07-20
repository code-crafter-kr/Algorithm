import sys
input = sys.stdin.readline

T = int(input())

direction_p  = [(1, 0), (-1, 0), (0, 1), (0, -1)]

directuon_x = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    best = 0
    # 모든 중심 좌표 순회
    for y in range(N):
        for x in range(N):
            # 중심 포함
            plus_sum  = board[y][x]
            cross_sum = board[y][x]

            # + 모양
            for dy, dx in direction_p:
                for step in range(1, M):
                    ny, nx = y + dy * step, x + dx * step
                    if 0 <= ny < N and 0 <= nx < N:
                        plus_sum += board[ny][nx]
                    else:      # 범위 벗어나면 그 방향 더 진행할 필요 없음
                        break

            # × 모양
            for dy, dx in directuon_x:
                for step in range(1, M):
                    ny, nx = y + dy * step, x + dx * step
                    if 0 <= ny < N and 0 <= nx < N:
                        cross_sum += board[ny][nx]
                    else:
                        break

            best = max(best, plus_sum, cross_sum)

    print(f"#{i} {best}")