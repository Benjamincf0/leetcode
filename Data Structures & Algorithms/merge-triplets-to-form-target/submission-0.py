class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [False, False, False]

        for triplet in triplets:
            cur_match = [False, False, False]
            for i in range(3):
                cur_match[i] = triplet[i] == target[i]
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    match[i] |= cur_match[i]
        
        return all(match)