class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output = 0

        nums_set = set(nums)

        for i in range(len(nums)):
            j = i
            if nums[j] - 1 not in nums_set:
                counter = 0
                num = nums[j]
                while num in nums_set:
                    counter += 1
                    num += 1
                
                output = max(counter,output)
        
        return output
