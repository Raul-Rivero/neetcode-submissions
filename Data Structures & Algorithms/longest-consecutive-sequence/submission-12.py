class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        cur = 0
        i = 0

        while i < len(nums):
            if nums[i]-1 not in numbers:
                temp = 0
                j = nums[i]
                while j in numbers:
                    temp += 1
                    j += 1
                cur = max(temp,cur)
            i += 1
        
        return cur
            