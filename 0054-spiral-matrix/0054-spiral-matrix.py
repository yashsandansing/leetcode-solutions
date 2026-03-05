class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        res = list()

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # go left if more than one row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            
            # go right if more than 2 columns
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        
        return res