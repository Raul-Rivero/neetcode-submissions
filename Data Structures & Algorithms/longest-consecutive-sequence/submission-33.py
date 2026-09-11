class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        output = 0

        for i in nums:
            j = i
            if j - 1 not in nums_set:
                num = j
                count = 1
                while num + 1 in nums_set:
                    num += 1
                    count += 1

                output = max(output,count)
        
        return output
