class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        reps = defaultdict(list)

        for s in strs:

            encode = [0] * 26

            for c in s:
                encode[ord(c) - ord('a')] += 1
            
            reps[tuple(encode)].append(s)

        return list(reps.values())