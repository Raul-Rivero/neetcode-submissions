class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for i in s:
            map_s[i] += 1
        for i in t:
            map_t[i] += 1 
        
        return map_s == map_t

