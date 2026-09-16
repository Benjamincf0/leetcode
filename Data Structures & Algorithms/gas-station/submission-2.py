class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy shit Time O(n) Space O(1)
        if sum(cost) > sum(gas): return -1

        start = 0
        partial_sum = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            partial_sum += g - c

            if partial_sum < 0:
                partial_sum = 0
                start = i+1

        return start