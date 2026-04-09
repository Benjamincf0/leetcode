class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        prev = None
        for i in range(len(nums)):
            while prev is not None and nums[i] == prev: i+=1
            prev = nums[i]

            left = i+1
            right = len(nums)-1

            target = -nums[i]

            while left < right:
                while left > i+1 and nums[left] == nums[left-1]: left+=1
                while right<len(nums)-1 and nums[right] == nums[right+1]: right-=1

                if nums[left]+nums[right] == target:
                    out.append([nums[i], nums[left], nums[right]])
                elif nums[left]+nums[right] > target:
                    right-=1
                else:
                    left+=1
        return out