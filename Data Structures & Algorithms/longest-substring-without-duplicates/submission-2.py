class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        tracker = set()

        res = 0

        i = 0
        j = 0

        while j < len(s):
            while s[j] in tracker:
                tracker.remove(s[i])
                i += 1
            tracker.add(s[j])
            j += 1

            res = max(res, len(tracker))

        return res
