import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for i in range (n):
    money = int(input())
    quater = money // 25
    dime = (money % 25) // 10
    nickel = ((money % 25) % 10) // 5
    print(quater, dime, nickel, ((money % 25) % 10) % 5)
