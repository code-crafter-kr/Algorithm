N, a, b = map(int, input().split())

idx = 0

def dfs(length, row, col):
    global idx


    if row == a and col == b:
        print(idx)
        return

    half = length // 2

    # 1사분면
    if a < row + half and b < col + half:
        dfs(half, row, col)

    # 2사분면
    elif a < row + half and b >= col + half:
        idx += half * half
        dfs(half, row, col + half)

    # 3사분면
    elif a >= row + half and b < col + half:
        idx += 2 * half * half
        dfs(half, row + half, col)

    # 4사분면
    else:
        idx += 3 * half * half
        dfs(half, row + half, col + half)

dfs(2 ** N, 0, 0)
