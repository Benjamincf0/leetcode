class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time O(n^2) Space O(1)
        for l in range(len(matrix)//2):
            r = len(matrix)-l-1

            for i in range(r-l):
                temp = matrix[l+i][r]
                matrix[l+i][r] = matrix[l][l+i]

                temp2 = matrix[r][r-i]
                matrix[r][r-i] = temp
                
                temp = matrix[r-i][l]
                matrix[r-i][l] = temp2

                matrix[l][l+i] = temp