import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        lst.append(temp)
    answer = 0
    # 완탐 시작
    for y in range(N):
        for x in range(N):
            result_p = 0
            result_x = 0
            # 상
            for y_idx in range(1, M):
                new_y = y - y_idx
                if new_y < 0:
                    continue
                else:
                    result_p += lst[new_y][x]
            # 하
            for y_idx in range(1, M):
                new_y = y + y_idx
                if new_y >= N:
                    continue
                else:
                    result_p += lst[new_y][x]
            # 좌
            for x_idx in range(1, M):
                new_x = x - x_idx
                if new_x < 0:
                    continue
                else:
                    result_p += lst[y][new_x]
            # 우
            for x_idx in range(1, M):
                new_x = x + x_idx
                if new_x >= N:
                    continue
                else:
                    result_p += lst[y][new_x]



            # 오른쪽 위
            for idx in range(1, M):
                new_y = y - idx
                new_x = x + idx
                if new_y < 0 or new_x >= N:
                    continue
                else:
                    result_x += lst[new_y][new_x]
            # 왼쪽 위
            for idx in range(1, M):
                new_y = y - idx
                new_x = x - idx
                if new_y < 0 or new_x < 0:
                    continue
                else:
                    result_x += lst[new_y][new_x]
            # 오른쪽 아래
            for idx in range(1, M):
                new_y = y + idx
                new_x = x + idx
                if new_y >= N or new_x >= N:
                    continue
                else:
                    result_x += lst[new_y][new_x]

            # 왼쪽 아래
            for idx in range(1, M):
                new_y = y + idx
                new_x = x - idx
                if new_y >= N or new_x < 0:
                    continue
                else:
                    result_x += lst[new_y][new_x]

            result_p += lst[y][x]
            result_x += lst[y][x]

            answer = max(answer, result_p, result_x)

    print(f"#{i+1}: {answer}")