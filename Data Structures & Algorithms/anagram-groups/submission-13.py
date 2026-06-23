class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        
        for s in strs:

            encoding = [0] * 26

            for c in s:
                encoding[ord(c) - ord('a')] += 1
            
            groups[tuple(encoding)].append(s)
        
        return [i for i in groups.values()]