class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search to find the row else return -1
            # do binary search on the row else return -1
        
        # or just convert 1d coords to 2d??

        l=0
        r=len(matrix)*len(matrix[0])-1

        while l<=r:
            mid = (l+r+1) // 2
            midVal = matrix[mid//len(matrix[0])][mid%len(matrix[0])]

            if target < midVal:
                r = mid-1
            elif target > midVal:
                l = mid+1
            else: return True
        return False