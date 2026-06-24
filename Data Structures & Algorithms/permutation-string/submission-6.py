class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_dict = defaultdict(int)

        for i in s1:
            s1_dict[i] += 1

        print(s1_dict)

        l = 0
        r = l + len(s1)

        while r < len(s2)+1:

            temp = defaultdict(int)

            r = l + len(s1)

            for i in s2[l:r]:
                temp[i] += 1
            
            print(temp)
            
            if temp == s1_dict:
                return True

            l += 1

        return False