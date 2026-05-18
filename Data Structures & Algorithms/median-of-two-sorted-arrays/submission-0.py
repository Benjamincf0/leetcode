class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        r1 = len(nums1)-1

        mid1 = (l1+r1)//2
        mid2 = (len(nums1)+len(nums2))//2 - mid1-1

        while l1 <= r1:
            if mid2<len(nums2) or mid1<len(nums1) or (nums1[mid1] <= nums2[mid2+1] and nums2[mid2] < nums1[mid2+1]):
                break
            elif nums1[mid1] > nums2[mid2+1]: # mid1 too high
                r1 = mid1-1
            elif nums2[mid2] > nums1[mid1+1]: # mid2 too high => mid1 too low
                l1 = mid1+1
            else: raise Exception("WOMPWOMP")

            mid2 = (len(num1)+len(nums2))//2 - mid1-1

        if (len(nums1)+len(nums2))%2 == 0:
            return (max(nums1[mid1], nums2[mid2]) + min(nums1[mid1+1], nums2[mid2+1]))//2
        else:
            max(nums1[mid1], nums2[mid2])