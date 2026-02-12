"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # approach
        # take mid
        # check each section -> if all 1s or 0s
        # if yes -> add a simple Node with vals
        # if no -> recursively go in deep

        def dfs(n, r, c):
            if n == 1:
                return Node(grid[r][c]==1, True)
            mid = n // 2
            top_left = dfs(mid, r, c)
            bottom_left = dfs(mid, r+mid, c)
            top_right = dfs(mid, r, c+mid)
            bottom_right = dfs(mid, r+mid, c+mid)

            if ((top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf) and
            top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)
            
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(len(grid), 0, 0)