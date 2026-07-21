class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:

            encode = [0] * 26

            for c in s:

                encode[ord(c) - ord('a')] += 1

            groups[tuple(encode)].append(s)

        output = []
        for i in groups.values():
            output.append(i)

        return output