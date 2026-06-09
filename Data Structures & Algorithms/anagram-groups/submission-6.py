class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:

            encode = [0] * 26

            for c in s:
                encode[ord(c) - ord('a')] += 1

            hashmap[tuple(encode)].append(s)

        output = []

        for i in hashmap.values():
            output.append(i)

        return output