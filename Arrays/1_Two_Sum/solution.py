class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        pair_index = {}
        for i , num in enumerate(nums):
            diff = target - num
            if diff in pair_index:
                return [ i , pair_index[diff]]
            pair_index[num] = i
    
# Testing the function
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target) 
print(result)  