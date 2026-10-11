class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        encodings = defaultdict(list)

        for s in strs:

            encoding = [0] * 26

            for c in s:
                encoding[ord("a") - ord(c)] += 1

            encodings[tuple(encoding)].append(s)

        
        return [i for i in encodings.values()]
        

