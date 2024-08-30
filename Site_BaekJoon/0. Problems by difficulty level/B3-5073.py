import sys
sys.stdin = open("input.txt", "r")

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    
    if max([a, b, c]) >= sum([a, b, c]) - max([a, b, c]):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles ")
    else:
        print("Scalene ")