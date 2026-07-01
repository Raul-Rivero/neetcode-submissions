class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tracker = set()
        counter = 0

        l = 0
        r = 0

        for i in range(len(s)):
            while s[i] in tracker:
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            r += 1
            counter = max(counter, r - l )
        
        return counter

        