import sys

def check(string):
    stk = []
    for c in string:
        if c == "(":
            stk.append("X")
        elif c == "[":
            stk.append("Y")

        elif c == ")":
            if "X" in stk and stk[-1] == "X":
                stk.pop()
            else:
                return "no"
        elif c == "]":
            if "Y" in stk and stk[-1] == "Y":
                stk.pop()
            else:
                return "no"

    if c != "." or stk != []:
        return "no"
    else:
        return "yes"

while True:
    a = input()
    if a == ".":
        break
    else:
        print(check(a))