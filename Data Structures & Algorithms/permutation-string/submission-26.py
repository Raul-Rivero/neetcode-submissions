class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        encode_s1, encode_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            encode_s1[ord(s1[i]) - ord('a')] += 1
            encode_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if encode_s1[i] == encode_s2[i]:
                matches += 1

        l = 0

        for r in range(len(s1),len(s2)):

            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            encode_s2[index] += 1

            if encode_s2[index] == encode_s1[index]:
                matches += 1
            elif encode_s1[index] == encode_s2[index] - 1:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            encode_s2[index] -= 1

            if encode_s2[index] == encode_s1[index]:
                matches += 1
            elif encode_s1[index] == encode_s2[index] + 1:
                matches -= 1

            l += 1

        return matches == 26