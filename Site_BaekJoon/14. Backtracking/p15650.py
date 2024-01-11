a, b = map(int, input().split())

temp = []
visited = [0] * (a + 1)

def back(x):

    if x == b + 1:
        print(" ".join([str(x) for x in temp]))
        return
    for i in range (1,a+1):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(i)
            back(x+1)
            temp.pop()
            for i in range (i+1, a+1): #i 이후로는 방문하지 않는것으로 처리 - 중복을 허용하지 않는다. 항상 오름차순이 만들어짐
                visited[i] = 0
        else:
            pass

back(1)
