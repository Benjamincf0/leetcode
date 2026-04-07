class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()

        for i in range(len(nums[:-2])):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    sums.append([nums[i], nums[l], nums[r]])

                    # skip duplicates first
                    while l < r and nums[l+1] == nums[l]: l+=1
                    while l < r and nums[r-1] == nums[r]: r-=1
                    
                    # go to next numbers
                    l += 1
                    r -= 1
                elif s > 0:
                    r-=1
                else:
                    l+=1
        return sums