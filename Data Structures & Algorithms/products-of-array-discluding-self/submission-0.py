class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        p = 1
        for num in nums:
            p *= num
            l.append(p)

        
        r = [1]
        p = 1
        for num in nums[::-1]:
            p *= num
            r.append(p)

        res = []

        for i in range(len(nums)):
            left = r[len(nums)-1-i]
            right = l[i]
            res.append(left*right)

        return res

        # l = 1, 2, 8, 48
        # r = 6, 24, 48, 48
