# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxInc = 0
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxInc
            if node is None:
                return 0
            leftInc = dfs(node.left)
            rightInc = dfs(node.right)

            inc = 1
            if node.left is not None and node.val - node.left.val == -1:
                inc = 1 + leftInc
            
            if node.right is not None and node.val - node.right.val == -1:
                inc = max(inc, 1 + rightInc)
            
            maxInc = max(maxInc, inc)
            return inc
        dfs(root)
        return maxInc