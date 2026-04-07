class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                numDays = i - stack[-1]
                out[stack[-1]] = numDays
                stack.pop()
            
            stack.append(i)
        
        return out