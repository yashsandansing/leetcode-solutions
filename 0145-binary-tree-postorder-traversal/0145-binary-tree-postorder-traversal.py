# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node is None:
                return
            # visit all left leaf nodes -> recursively add child parents
            # last to be added should be root
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
            return
        
        dfs(root)
        return res