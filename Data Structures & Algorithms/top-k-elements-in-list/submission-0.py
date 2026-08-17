class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        freqs = [[] for _ in range(len(nums))]

        for num, freq in d.items():
            freqs[freq-1].append(num)

        res = []
        for nums_w_freq in reversed(freqs):
            while nums_w_freq:
                res.append(nums_w_freq.pop())
                if len(res) == k:
                    return res

        return res