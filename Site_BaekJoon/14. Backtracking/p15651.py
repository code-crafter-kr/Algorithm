a, b = map(int, input().split())

lst = []
temp = []
def back(x):

    if x == b + 1:
        lst.append(temp.copy())
        return

    for i in range (1,a+1):
        temp.append(i)
        back(x+1)
        temp.pop()

back(1)
for i in lst:
    print(* i)