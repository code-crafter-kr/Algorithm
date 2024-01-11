import sys
sys.stdin = open("input.txt", "r")

def stack():
    X = int(sys.stdin.readline()) #총횟수 받기
    list_C = []
    list_X = [] #push와 pop을 메모
    y = 1
    
    for _ in range (X):
        i = int(sys.stdin.readline()) #4,3,6,8,7,5,2,1
        
        while True:
            if i in list_C:
                o = list_C.pop() #C에 든 그릇에 있는것을 D로 pop
                if o == i:
                    list_X.append("-") # (2) - -  (4) -
                    break
                
                else:
                    print("NO")
                    exit()

            else:
                for x in range (y,i + 1): # (1,5) # 5, 6
                    list_C.append(x) # [1,2,3,4] > [1, 2] > [1,2,5,6] > [1,2,5] > [1,2,5,7,8]
                    list_X.append("+") # (1) + + + + (3) + + (5) + +
                y = i + 1

    print("\n".join(list_X))

stack()
