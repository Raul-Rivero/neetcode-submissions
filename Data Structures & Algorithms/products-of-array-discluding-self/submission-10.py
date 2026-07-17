class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prefix
            prefix *= nums[i]

        return output

# [1,2,4,6]

# [1,1,2,8]

# [48,24,6,1]

# [48,24,12,8]