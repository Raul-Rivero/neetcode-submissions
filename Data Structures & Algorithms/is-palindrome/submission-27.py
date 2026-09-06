class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            
            while not s[l].isalnum() and l < len(s) - 1:
                l += 1

            while not s[r].isalnum() and r > 0 :
                r -= 1

            if not l < r:
                break
            
            if s[r].lower() != s[l].lower():
                print(s[l],s[r])
                return False
            else:
                r -= 1
                l += 1
        
        return True
