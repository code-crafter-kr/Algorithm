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
            visited[i] = 0
        else:
            pass

back(1)
