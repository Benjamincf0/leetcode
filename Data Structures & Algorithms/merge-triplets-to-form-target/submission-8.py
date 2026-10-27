class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a = b = c = False

        for u, v, w in triplets:
            if u <= x and v <= y and w <= z:
                    a |= u == x
                    b |= v == y
                    c |= w == z
            if a and b and c: return True
        
        return False