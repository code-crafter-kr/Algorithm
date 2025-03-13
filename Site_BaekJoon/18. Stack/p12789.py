from collections import deque
n = int(input())

lst = deque(map(int, input().split()))
stack = []

# stack은 반드시 내림차순 형태이며 단순히 맨위의 element가 새로들어올 element보다 커야한다.
target_person = 1
while True:
    if not lst:
        print("Nice")
        break

    while stack:
        if stack[-1] == target_person:
            target_person += 1
            stack.pop()
        else:
            break

    next_person = lst.popleft() # 가장 앞에 있는 사람을 뽑아옴

    if next_person == target_person: # 가장 이상적일 때.
        target_person += 1
        continue

    else:
        try:
            if stack[-1] < next_person: # 더 큰수가 들어올 때 = 스택이 망가질 때 = 절대 풀 수 없음.
                print("Sad")
                break
            else:
                stack.append(next_person)
        except:
            stack.append(next_person)
