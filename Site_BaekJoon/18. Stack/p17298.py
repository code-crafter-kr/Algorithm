#index값을 저장할것
import sys
sys.stdin = open("input.txt", "r")
#4 2 3 1 8
n = int(sys.stdin.readline())

def osu(n):
    list_A = list(map(int,input().split()))
    answer = [-1 for _ in range (n)]
    stack = [0]
    for i in range (1, n):
        if list_A[stack[-1]] >= list_A[i]:
            stack.append(i)

        else:
            while len(stack) > 0 and list_A[stack[-1]] < list_A[i]:
                answer[stack.pop()] = list_A[i]
            stack.append(i)
            
    print(* answer)


osu(n)




# import sys
# sys.stdin = open("input.txt", "r")
# n = int(sys.stdin.readline())

# def osu():
#     list_A = list((map(int, sys.stdin.readline().split())))
#     a = 0

#     for ii in range (len(list_A)):

#         for jj in range (ii+1, len(list_A)):
#             if list_A[jj] > list_A[ii]:
#                 print(list_A[jj], end = " ")
#                 a = a + 1
#                 break

#         if a != ii+1:
#             print(-1, end = " ")
#             a = a + 1

# osu()


# import sys
# sys.stdin = open("input.txt", "r")

# n = int(sys.stdin.readline())

# def osu(x):
#     list_A = list((map(int, sys.stdin.readline().split())))
#     a = 0

#     for i in range (x):
#         x = list_A.pop(0)
#         a = 0
#         while True:
            
#             if list_A == []:
#                 print(-1)
#                 break

#             elif a == len(list_A):
#                 print(-1, end = " ")
#                 break

#             elif x < list_A[a]:
#                 print(list_A[a], end = " ")
#                 break
    
#             else:
#                 a = a + 1
# osu(n)
