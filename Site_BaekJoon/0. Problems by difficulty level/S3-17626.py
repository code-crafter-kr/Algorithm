import math
n = int(input())

dp = [0] * 50001

for i in range(1, int(math.sqrt(50001)+1)):
    dp[i**2] = 1




print(dp[n])