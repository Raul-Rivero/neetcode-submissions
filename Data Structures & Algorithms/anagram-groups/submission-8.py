class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        reps = defaultdict(list)

        for s in strs:

            encode = [0] * 26

            for c in s:
                encode[ord('a') - ord(c)] += 1
            
            reps[tuple(encode)].append(s)
        
        output = []
        for i in reps.values():
            output.append(i)

        return output