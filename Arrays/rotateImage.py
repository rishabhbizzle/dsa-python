class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # tranpose the matrix then reverse each row

        cols = len(matrix[0])
        rows = len(matrix)

        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            s = 0
            e = cols - 1
            while s < e:
                matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
                s += 1
                e -= 1
