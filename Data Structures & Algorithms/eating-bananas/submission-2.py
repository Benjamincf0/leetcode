class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        for k in range(1, maximum):
            hours=0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours<=h: return k
        return maximum