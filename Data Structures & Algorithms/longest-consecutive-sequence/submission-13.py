class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cur = 0

        numbers = set()

        for i in nums:
            numbers.add(i)

        for i in nums:
            j = i
            temp = 1
            if j-1 not in numbers:
                while j + 1 in numbers:
                    j += 1
                    temp += 1

            cur = max(cur,temp)
        
        return cur


