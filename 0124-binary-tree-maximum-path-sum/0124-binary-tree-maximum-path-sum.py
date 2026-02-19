# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs -> node is None: return 0
        # res = max(res, l + r + node.val)
        # return max(node.val + max(l, r), 0)

        res = float('-inf')

        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            res = max(res, l + r + node.val)

            return max(0, node.val + max(l, r))
        dfs(root)
        return res
