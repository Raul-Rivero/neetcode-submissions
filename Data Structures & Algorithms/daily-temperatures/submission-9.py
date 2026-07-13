class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] #index,temp

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                index,temp = stack.pop()
                output[index] = i - index
            stack.append([i,t])

        return output