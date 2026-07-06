class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cur = 0
        nums_set = set()

        for i in nums:
            nums_set.add(i)

        for i in nums:
            tracker = set()
            if i - 1 not in nums_set:
                tracker.add(i)
                while i + 1 in nums_set:
                    tracker.add(i + 1)
                    i += 1
            
            cur = max(cur,len(tracker))
        
        return cur
            


