import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())
hash_company = {}
lst = set()
for i in range (n):
    name, status = input().split()
    lst.add(name)
    if status == "enter":
        hash_company[name] = True
    else:
        hash_company[name] = False

lst = list(lst)
lst.sort(reverse = True)

for i in lst:
    if hash_company[i] == True:
        print(i)