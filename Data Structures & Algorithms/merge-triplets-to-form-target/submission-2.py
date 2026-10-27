class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [False, False, False]

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    match[i] |= triplet[i] == target[i]
        
        return all(match)