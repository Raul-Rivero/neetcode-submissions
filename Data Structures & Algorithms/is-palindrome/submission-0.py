class Solution:
    def isPalindrome(self, s: str) -> bool:
        dir_1 = []
        dir_2 = []

        for c in s:
            if c.isalpha():
                dir_1.append(c.lower())
            if c.isdigit():
                dir_1.append(c)

        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                dir_2.append(s[i].lower())
            if s[i].isdigit():
                dir_2.append(c)


        print(dir_1)
        print(dir_2)
        return dir_1 == dir_2

