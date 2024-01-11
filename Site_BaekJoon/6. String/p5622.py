# 문자열 문제 '다이얼'
Dial = input()
A = 0

for i in Dial:
    if i in ["A" ,"B", "C"]:
        A = A + 3
    if i in ["D" ,"E", "F"]:
        A = A + 4
    if i in ["G" ,"H", "I"]:
        A = A + 5
    if i in ["J" ,"K", "L"]:
        A = A + 6
    if i in ["M" ,"N", "O"]:
        A = A + 7
    if i in ["P" ,"Q", "R" , "S"]:
        A = A + 8
    if i in ["T", "U" ,"V"]:
        A = A + 9
    if i in ["W" ,"X", "Y", "Z"]:
        A = A + 10

print(A)