class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring_set = set()
        output = 0
        l = 0
        r = 0

        while r < len(s):

            if s[r] in substring_set:
                output = max(output, r - l)
                substring_set.remove(s[l])
                l += 1
            
            else:
                substring_set.add(s[r])
                r += 1

        output = max(output, r - l)

        return output
            
            