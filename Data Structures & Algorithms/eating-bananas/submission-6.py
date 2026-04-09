class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l <= r:
            mid = (l+r+1) // 2 # = k
            midVal = 0 # = h
            for pile in piles:
                midVal+= math.ceil(pile/mid)
                print(math.ceil(pile/mid ))
            print(midVal, 2, math.ceil(3/2), piles)

            if h > midVal:
                l = mid+1
            elif h < midVal:
                r = mid-1
            else:
                return mid
        return mid-1