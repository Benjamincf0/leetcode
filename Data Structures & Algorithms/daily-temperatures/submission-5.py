class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                popped_idx = stack.pop()
                numDays = i - popped_idx
                out[popped_idx] = numDays
            
            stack.append(i)
        
        return out