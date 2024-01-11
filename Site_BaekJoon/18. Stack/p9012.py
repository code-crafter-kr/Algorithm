import sys
sys.stdin=open('input.txt','r')

N = int(input())
for i in range (N):
    stk = []
    a = input()
    a = list(a)
    z = 0
    for ii in a:
        if ii == "(":
            stk.append("x")
        else:
            if stk == []:
                print("NO")
                z = 1
                break
            else:
                stk.pop()
    
    if z != 1:
        if len(stk) == 0:
            print("YES")
        else:
            print("NO")

import sys
sys.stdin=open('input.txt','r')
def check(string):
    stk = []
    for c in string:
        if c == '(':
            stk.append("*")
        elif (c == ')') and len(stk)==0:
            return "NO"
        elif (c==')') and len(stk)>=1:
            stk.pop()
    return "YES" if len(stk)==0 else "NO"

input=sys.stdin.readline
T = int(input())
for ii in range(T):
    print(check(input()))
