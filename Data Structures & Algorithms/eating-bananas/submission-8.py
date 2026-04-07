class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2 # k
            midVal = 0 # hours
            for pile in piles:
                midVal+= math.ceil(pile/mid)

            if h >= midVal:
                r = mid-1
                res = mid
            else:
                l = mid+1
        return res