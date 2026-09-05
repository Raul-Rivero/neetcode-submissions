class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        output = 0
        
        nums_set = set(nums)

        for i in nums:
            counter = 0
            if i-1 not in nums_set:
                j = i
                while j in nums_set:
                    counter += 1
                    j += 1


            output = max(output,counter)
        
        return output