class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = 10**5
        for i in prices:
            if i < minimum:
                minimum = i
            profit = max(profit, i - minimum)
        return profit