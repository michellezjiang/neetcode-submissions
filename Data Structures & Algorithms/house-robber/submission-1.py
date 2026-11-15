class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * (len(nums)+1)

        dp[1] = nums[0]
        if len(nums) < 2:
            return dp[1]
        dp[2] = max(nums[1], nums[0])

        for i in range(3, len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        print(dp)
        return dp[len(nums)]

        