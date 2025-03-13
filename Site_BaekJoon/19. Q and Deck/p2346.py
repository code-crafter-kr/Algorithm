from collections import deque
n = int(input())
lst = deque([i for i in range(1, n + 1)])
content = (list(map(int, input().split())))

dic = {}

for i in range (0, n):
    dic[i + 1] = content[i]
print(dic)

for i in range(n-1):
    target_ballon = lst.popleft()
    print(target_ballon, end = " ")
    next_number = dic[target_ballon]
    if next_number > 0:  # 오른쪽으로 이동
        for _ in range(next_number - 1):
            lst.append(lst.popleft())
    elif next_number < 0:  # 왼쪽으로 이동
        for _ in range(abs(next_number)):
            lst.appendleft(lst.pop())

print(lst[0])
