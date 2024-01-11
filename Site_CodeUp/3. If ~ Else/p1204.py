A = int(input())
print("%dth" %A if A in [11, 12, 13] else "%dst" %A if A%10 == 1 else "%dnd" %A if A%10 == 2 else "%drd" %A if A%10 == 3 else "%dth" %A)