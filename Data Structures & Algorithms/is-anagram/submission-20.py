class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        trackerS = defaultdict(int)
        trackerT = defaultdict(int)

        for i in s:
            trackerS[i] += 1

        for i in t:
            trackerT[i] += 1

        return trackerT == trackerS