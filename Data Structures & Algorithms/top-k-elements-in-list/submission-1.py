class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort strat. Time is O(n) ; Space O(n)
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        freqs = [[] for _ in range(len(nums))]

        for num, freq in d.items():
            freqs[freq-1].append(num)

        res = []
        for nums_w_freq in reversed(freqs):
            for num in nums_w_freq:
                res.append(num)
                if len(res) == k:
                    return res

        return res