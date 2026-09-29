class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        elements = {")":"(","}":"{","]":"["}

        for i in s:
            if i not in elements:
                stack.append(i)
            else:
                if stack and elements[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False

