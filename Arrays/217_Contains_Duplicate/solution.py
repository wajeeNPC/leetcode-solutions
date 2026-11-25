class Solution(object):

    def containsDuplicateV1(self, nums) -> bool :
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicateV2(self , nums ) -> bool :
        temp_value = {}
        for i , value in enumerate(nums):
            if value in temp_value :
                return True
            temp_value[value] = i
        return False

    def containsDuplicateV3(self , nums ) -> bool :
        seen = set()
        for value in nums:
            if value in seen :
                return True
            seen.add(value)
        return False

    def containsDuplicateV4(self , nums ) -> bool :
        nums = sorted(nums)
        for i in range (1 , len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


solution = Solution()
result = solution.containsDuplicateV2([1,2,3, 2])
print(result)