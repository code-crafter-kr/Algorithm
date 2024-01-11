import sys
sys.stdin = open("input.txt", "r")


M = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
list_B =list(map(int, sys.stdin.readline().split()))

ans = list(map(lambda n : n in list_A, list_B))

for _ in range(0, M):
    print("%d"%ans[_], end=" ")     
