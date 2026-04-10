class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # -1 0 2 4 6 8
        #  0 1 2 3 4 5
        #        lr
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2

            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else: return m
        
        return -1