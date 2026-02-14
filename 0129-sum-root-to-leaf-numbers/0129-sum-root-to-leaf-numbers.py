# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            # base case -> if we ever hit None
            if node is None:
                return 0
            
            # top-down, pass our path by multiplying
            # with 10 for each depth
            path = path*10 + node.val

            # if leaf node, return newly calculated path
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)