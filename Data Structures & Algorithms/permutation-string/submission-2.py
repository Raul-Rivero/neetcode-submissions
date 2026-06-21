class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        map_s1 = defaultdict(int)
        for i in s1:
            map_s1[i] += 1

        print(map_s1)

        l = 0
        r = l + len(s1)

        while r < len(s2)+1:
            map_temp = defaultdict(int)
            r = l + len(s1)
            print(s2[l:r])
            for i in s2[l:r]:
                map_temp[i] += 1
            print(map_temp)
            if map_temp == map_s1:
                return True
            l += 1

        return False
