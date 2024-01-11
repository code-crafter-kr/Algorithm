a, b = map(int, input().split())

temp = []
visited = [0] * (a + 1)

def back(x):

    if x == b + 1:
        print(" ".join([str(x) for x in temp]))
        return

    for i in range (1,a+1):
        if visited[i] == 0:
            temp.append(i)
            back(x+1)
            visited[i] = 1 # 방문을 back 트래킹이 끝난이후로 처리 > 중복으로 방문을 허용한다.
            temp.pop()
            for i in range (i+1, a+1): 
                visited[i] = 0
        else:
            pass

back(1)
