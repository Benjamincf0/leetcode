class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x: x[0])

        stack = []
        for pos, speed in pairs[::-1]:
            timeToTarget = (target-pos)/speed

            if not stack or timeToTarget > stack[-1]: stack.append(timeToTarget) # current is faster than next (or empty stack)

        return len(stack)