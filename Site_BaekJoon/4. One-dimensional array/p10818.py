N = int(input())

A_list = input() . split()
A_list = list(map( int , A_list))
A_list.sort()

print(A_list[0] , A_list[-1])