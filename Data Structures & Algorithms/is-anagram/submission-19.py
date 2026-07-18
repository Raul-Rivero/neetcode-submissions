class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for i in s:
            hash_s[i] += 1
        
        for i in t:
            hash_t[i] += 1

        if hash_s == hash_t:
            return True
        
        return False
