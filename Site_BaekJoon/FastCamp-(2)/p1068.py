import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

relation = {} # 해당 노드가 어떤 자식을 가지는지

for i in range(n): #모든 노드는 일단 자식을 가질 수 있는 가능성이 있다.
    relation[i] = []

for i in range (n):
    if lst[i] == -1:
        root = i #루트노드가 어디서 시작인지 체크한다

    elif i == x: #제거되는 노드는 아에 기록하지 않는다
        continue

    else: #모든 자식노드를 기록한다.
        parent_node = lst[i]
        node_number = i
        relation[parent_node].append(node_number)


cnt = 0 # 전체 카운트

def count_leaf_dfs(parent):
    global cnt
    
    children = relation[parent]
    if children == []: # 자식노드가 없다는건... 리프노드라는 뜻
        cnt += 1
        return
    else:
        for i in children: # 자식 노드가 있으면 cnt
            count_leaf_dfs(i)
    return

count_leaf_dfs(root)

if x == root:
    print(0, end = "")
else:
    print(cnt, end = "")