class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        totalProduct = 1
        for num in nums:
            totalProduct *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = 1
                newList = nums[:i] + nums[i+1:]
                for num in newList:
                    temp *= num
                output.append(temp)
            else:
                output.append(totalProduct//nums[i])


        return output
        