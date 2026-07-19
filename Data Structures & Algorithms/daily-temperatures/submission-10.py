class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = [] #[index,temperatures]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][-1] < t:
                stackIndex, stackTemp = stack.pop()
                output[stackIndex] = i - stackIndex
            stack.append([i,t])

        return output
