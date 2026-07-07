class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = 0

        tracker = set()

        l = 0

        for r in range(len(s)):
            
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1

            tracker.add(s[r])
            
            cur = max(cur,len(tracker))
        
        return cur


