class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cur = 0
        tracker = 0

        set_nums = set()

        for i in nums:
            set_nums.add(i)

        for i in range(len(nums)):
            if nums[i] - 1 not in set_nums:
                tracker = 1
                number = nums[i]
                while number + 1 in set_nums:
                    tracker += 1
                    number += 1
            
            cur = max(cur,tracker)

        return cur