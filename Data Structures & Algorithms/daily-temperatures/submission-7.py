class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)

        stack = [] # [index,temp]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackIndex, tempIndex = stack.pop()
                output[stackIndex] = i - stackIndex
            stack.append([i,t])
        
        return output