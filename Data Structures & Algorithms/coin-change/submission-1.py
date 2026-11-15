class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount+1):
            numCoins = []
            for coin in coins:
                if i - coin < 0:
                    continue
                if dp[i-coin] == -1:
                    continue

                else:
                    numCoins.append(1+dp[i-coin])

            if numCoins == []:
                dp[i] = -1

            else:
                dp[i] = min(numCoins)
        return dp[amount]
