class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbas = set(nums)
        max_len = 0

        for num in nums:
            if num-1 not in numbas:
                l = 0
                while num in numbas:
                    num+=1
                    l += 1
                max_len = max(max_len, l)

        return max_len