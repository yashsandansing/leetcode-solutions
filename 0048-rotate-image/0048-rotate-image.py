class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        first = 0
        last = n - 1
        
        while first < last:
            for c in range(n):
                temp = matrix[first][c]
                matrix[first][c] = matrix[last][c]
                matrix[last][c] = temp

            first += 1
            last -= 1

        for r in range(n):
            for c in range(r+1, n):
                # print((r, c), (c, r))
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        