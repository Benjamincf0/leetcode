class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        mc = 0
        mi = -1
        for i, c in counts.items():
            if c > mc:
                mi = i
                mc = c
        
        return mi