# Time complexity: O(m*n)
# Space complexity: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zeroRows = [0 for i in range(rows)]
        zeroCols = [0 for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    #marking which row and column need to be zero
                    zeroRows[i] = 1
                    zeroCols[j] = 1

        for i in range(rows):
            for j in range(cols):
                if zeroRows[i] == 1 or zeroCols[j] == 1:
                    matrix[i][j] = 0