class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices) - 1):
            buy = prices[i]
            sell = max(prices[i+1:])
            maxP = max(maxP, sell-buy)

        return maxP