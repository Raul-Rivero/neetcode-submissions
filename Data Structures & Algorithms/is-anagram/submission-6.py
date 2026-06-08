class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
        
        hashset1 = defaultdict(int)
        hashset2 = defaultdict(int)

        for i in s:
            hashset1[i] += 1

        for i in t:
            hashset2[i] += 1

        return hashset1 == hashset2