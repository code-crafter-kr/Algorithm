import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))


white = 0
blue = 0

def section(paper):
    half = len(paper) // 2
    a = [row[:half] for row in paper[:half]]
    b = [row[half:] for row in paper[:half]] 
    c = [row[:half] for row in paper[half:]]
    d = [row[half:] for row in paper[half:]]
    
    return a, b, c, d

def checker(paper):
    color = paper[0][0]

    for row in paper:
        for pixel in row:
            if pixel != color:
                return "m"
    
    if color == 0:
        return "w"
    else:
        return "b"

def dfs(paper):
    global white
    global blue

    paper_type = checker(paper)

    if paper_type == "w":
        white += 1
        return

    elif paper_type == "b":
        blue += 1
        return
    a, b, c, d = section(paper)
    dfs(a)
    dfs(b)
    dfs(c)
    dfs(d)


dfs(lst)
print(white)
print(blue)