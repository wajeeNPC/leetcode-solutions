class Solution(object):

    def twoSumV1(self , nums , target) :
        for i in range(len(nums)):
            for j  in range(i + 1 , len(nums)):
                if target == nums[i] + nums[j] :
                    return [i , j]
        return []

    def twoSumV2(self , nums , target) :
            pair_index = {}
            for index , value in enumerate(nums):
                 diff = target - value
                 if diff in pair_index:
                      return [ index , pair_index[diff]]
                 pair_index[value] = index  
            return []

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSumV2(nums, target) 
print(result) 