class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        l = 0
        r = len(A)-1

        while True:
            midA = (l+r)//2
            midB = (len(A)+len(B))//2 - midA - 2

            ALeft = A[midA] if -1<midA else float('-inf')
            ARight = A[midA+1] if midA+1<len(A) else float('inf')

            BLeft = B[midB] if -1<midB else float('-inf')
            BRight = B[midB+1] if midB+1<len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if (len(A)+len(B))%2 == 0:
                    return (max(ALeft, BLeft)+min(ARight, BRight))/2
                else:
                    return min(ARight, BRight)
            elif ALeft > BRight: #midA too large
                r = midA-1
            elif BLeft > ARight:
                l = midA+1
