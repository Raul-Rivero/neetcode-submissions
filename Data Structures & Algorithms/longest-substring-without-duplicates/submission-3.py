class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp_set =set()
        cur = 0

        l = 0

        for r in range(len(s)):
            while s[r] in temp_set:
                temp_set.remove(s[l])
                l += 1
            temp_set.add(s[r])
            cur = max(cur, r - l + 1)

        return cur