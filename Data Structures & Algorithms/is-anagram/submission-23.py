class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in s:
            dict1[i] += 1

        for i in t:
            dict2[i] += 1

        return dict1 == dict2
            