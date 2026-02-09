# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            # will return none for empty trees
            if node is None:
                return
            # every leaf node follows this pattern
            # so all elements will be added inorder
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res