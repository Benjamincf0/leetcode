class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, spd) for pos, spd in zip(position, speed)]
        pairs.sort(key=lambda x: x[0])

        def intersects(i, j) -> bool:
            xi = pairs[i][0]
            vi = pairs[i][1]
            xj = pairs[j][0]
            vj = pairs[j][1]
            if vi == vj:
                return False
            p = xi + vi * (xi - xj) / (vj - vi)
            # print(f"intersects: {i} & {j} : xi:{xi} vi:{vi} xj:{xj} vj:{vj} ? {p <= target and p > 0}")
            return p <= target and p > xi

        stack = [0]
        for i in range(1, len(pairs)):
            while stack and intersects(i, stack[-1]):
                stack.pop()
            stack.append(i)

        return len(stack)
