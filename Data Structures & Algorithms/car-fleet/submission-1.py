class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, spd) for pos, spd in zip(position, speed)]
        pairs.sort(key=lambda x: x[0])

        print(pairs)

        def intersects(i, j) -> bool:
            xi = pairs[i][0]
            vi = pairs[i][1]
            xj = pairs[j][0]
            vj = pairs[j][1]
            if vi == vj: return False
            p = xi + vi*(xi-xj)/(vj-vi)
            print(p)
            return p <= target and p > 0

        stack = [0]
        for i in range(1, len(pairs)):
            inter = intersects(i, stack[-1])
            print(f"intersects: {i} & {stack[-1]} ? {inter}")
            while stack and inter: stack.pop()
            stack.append(i)
        
        return len(stack)