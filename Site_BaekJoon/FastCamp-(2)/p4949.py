import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def check(sentence):
    if sentence[-1] != ".": # correct algorithm
        return False
    
    stk = []
    for char in sentence:
        if char in "([":
            stk.append(char) # add character
        elif char in ")]":
            if not stk: 
                return False
            if char == ")" and stk[-1] != "(": # check the last stack element
                return False
            if char == "]" and stk[-1] != "[":
                return False
            stk.pop()
    return len(stk) == 0


while True:
    sentence = input().rstrip()
    if sentence == ".": # 종료 조건
        break

    if check(sentence): # if it is True, print (YES)
        print("yes")
    else: # if it is False, print (NO)
        print("no")

