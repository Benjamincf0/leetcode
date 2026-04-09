class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 6 1 2
        #         lr
        # 0 1 2 3 4 5

        # if nums[0] < nums[-1]: return nums[0] # since array must be sorted

        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r+1)//2

            if nums[mid] < nums[l]: # min must be in left half
                r = mid
            elif nums[mid] > nums[r]: # min must be in right half
                l = mid+1
            else: break
        return nums[l]