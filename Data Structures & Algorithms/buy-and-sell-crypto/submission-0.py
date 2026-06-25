class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                curr = prices[j] - prices[i]
                if curr > best:
                    best = curr


        return best
        