class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestRun = 0
        
        numSet = set(nums)
        for num in numSet:
            count = 0
            if num - 1 not in numSet:
                while count + num in numSet:
                    count += 1

            if count > longestRun:
                longestRun = count

        return longestRun

            
        