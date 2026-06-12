class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        prefix = 1
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            output[i] *= prefix

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
             
        return output

    
#  1  2  4 6
#  1  1  2 8 pre
# 48 24  6 1 post 
# 48 24 12 8