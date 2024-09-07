import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input()) # 2이상 동기들의 수
m = int(input()) # 다음 입력 개수

relation = {}
for i in range (1, n+1): #자신과 마지막 동기까지 포함
    relation[i] = []

result = set()

for i in range (m):
    a, b = map(int, input().split()) # a랑 b랑 친구
    relation[a].append(b)
    if a == 1:
        result.add(b) # 직접 친구 바로 추가
    relation[b].append(a)

ans = set()

for i in result:
    for x in relation[i]:
        ans.add(x) # 간접 1차친구 추가

result.update(ans)
if 1 in ans:
    print(len(result)-1, end = "")
else:
    print(len(result), end = "")