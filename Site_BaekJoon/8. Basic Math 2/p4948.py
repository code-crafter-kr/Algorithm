
import sys
sys.stdin=open('input.txt','r')
                        
def deter(a): #소수 리스트를 뽑아주는 def 함수 (1부터 a까지의 소수 리스트를 뽑아준다)
    if a == 1:
        return False
    else:
        for n in range(2, int(a**0.5)+1):
                if a % n == 0 :
                    return False
                    
        return True

list_A =[]
 
for i in range (1, 123456*2):
    if deter(i):
        list_A.append(i)

while True:
    list_B = []
    A = int(sys.stdin.readline())

    if A == 0:
        break
    for i in list_A:
        if i >= A+1 and i <= 2*A:
            list_B.append(i)

    print(len(list_B))
    



        



