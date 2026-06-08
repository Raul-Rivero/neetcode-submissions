class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashset1 = list()
        hashset2 = list()

        for i in s:
            hashset1.append(i)

        for j in t:
            hashset2.append(j)
        
        if sorted(hashset1) == sorted(hashset2):
            return True

        return False