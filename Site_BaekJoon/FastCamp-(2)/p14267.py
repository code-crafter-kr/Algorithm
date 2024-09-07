import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0] + list(map(int, input().split())) #직원은 0번이 아닌 1번부터 시작한다는것을 dummy를 추가하여 보정

compliment_list = [0 for _ in range (n + 1)]

for _ in range (m):
    employee, compliment = map(int, input().split())
    compliment_list[employee] += compliment


total_compliment = [0 for _ in range (n+1)]
for i in range (1, n):
    employee = i + 1 #2번 직원부터 시작해서 5번직원까지..
    total_compliment[employee] = total_compliment[lst[employee]] + compliment_list[employee]

print(*total_compliment[1:], end = " ")