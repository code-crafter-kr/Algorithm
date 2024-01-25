class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Populate the DP array
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]