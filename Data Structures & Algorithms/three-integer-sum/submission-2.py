class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort() #O(n*log(n))

        i=0
        j=len(nums)-1

        while i<j: # O(n)
            n1 = nums[i]
            n2 = nums[j]
            psum = n1+n2
            target = -psum

            if target < n1: # psum is too big
                j-=1
            elif target > n2: # psum is too small
                i+=1
            else: # target could be somewhere in the middle -> binary search O(log(n))
                p = i+1
                q = j-1
                foundAt = -1
                while p<=q:
                    mid = (p+q+1)//2
                    if nums[mid] == target:
                        foundAt = mid
                        break
                    elif nums[mid] > target:
                        q = mid
                    else:
                        p = mid
                
                if foundAt != -1:
                    out.append([n1, target, n2])