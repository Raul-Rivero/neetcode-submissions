class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        goal = defaultdict(int)
        for i in s1:
            goal[i] += 1

        l = 0

        r = l + len(s1)

        while r < len(s2)+1:
            r = l + len(s1)
            temp = defaultdict(int)
            
            for i in s2[l:r]:
                temp[i] += 1

            if temp == goal:
                return True

            l += 1

        return False
            