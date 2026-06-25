class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestRun = 0
        
        numSet = set(nums)
        for num in nums:
            currRun = 0
            if num - 1 not in numSet:
                while num + currRun in numSet:
                    currRun += 1

            if currRun > longestRun:
                longestRun = currRun
            currRun = 0

        return longestRun

            
        