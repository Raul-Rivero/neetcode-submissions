class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cur = set()

        i = 0

        out = 0

        for j in range(len(s)):
            while s[j] in cur:
                cur.remove(s[i])
                i += 1
            cur.add(s[j])
            out = max(out, j - i + 1)
        return out