class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 5 6 0 1 2
        # 0 1 2 3 4 5
        #   r l
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] == target: return m
            elif nums[l] <= nums[m]: # left half increasing
                if nums[l] <= target and target < nums[m]: # target E [l, m)
                    r = m-1
                else: # target E (m, r]
                    l = m+1
            else: # right half increasing
                if nums[m] < target and target <= nums[r]: # target E (m, r]
                    l = m+1
                else: # target E [l, m)
                    r = m-1
        return -1