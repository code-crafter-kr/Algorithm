class Solution(object):
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # base step
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                # dp[i - 1][j]는 i-1개의 원소로 j개의 역쌍을 가질 수 있는 경우의 수
                val = dp[i - 1][j]
                
                # 만약 j - i >= 0이면, 즉 현재 원소를 추가할 때 j개 이상의 역쌍을 생성할 수 있는 경우
                if j - i >= 0:
                    # dp[i - 1][j - i]를 빼줍니다. 이는 새로 추가되는 원소가 기존 리스트의 역쌍에 영향을 줄 수 있는 경우를 제거하기 위함입니다.
                    val = val - dp[i - 1][j - i]
                
                # 모듈러 연산 적용
                val = (val + MOD) % MOD
                
                # 이전에 계산된 dp[i][j-1]에 현재 val 값을 더해줍니다. 이는 j개의 역쌍을 가지는 경우의 수를 누적시키는 과정입니다.
                dp[i][j] = (dp[i][j - 1] + val) % MOD

        return (dp[n][k] - dp[n][k - 1]) % MOD