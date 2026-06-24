class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cur = 0
        temp_set = set()

        l = 0 
        r = 0

        for r in range(len(s)):
            while s[r] in temp_set:
                temp_set.remove(s[l])
                l += 1
            temp_set.add(s[r])
            cur = max(cur, r - l + 1)

        return cur