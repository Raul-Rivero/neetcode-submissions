class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        cur = 0

        num_set = set(nums)

        for i in nums:
            tracker = []

            if (i - 1) not in num_set:
                tracker.append(i)
                j = i

                while j + 1 in num_set:
                    tracker.append(j + 1)
                    j += 1
            
            cur = max(cur,len(tracker))
        
        return cur