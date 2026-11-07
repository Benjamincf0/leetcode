class Solution:
    def jump(self, nums: List[int]) -> int:
        res=l=r=0

        while r < len(nums)-1:
            farthest = max(i+nums[i] for i in range(l,r+1))
            l, r = r+1, farthest
            res+=1

        return res