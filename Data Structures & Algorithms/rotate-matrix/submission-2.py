class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """[[1,2],[3,4]]  [[3,1],[2,4]]

        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for mat in matrix:
            mat.reverse()

