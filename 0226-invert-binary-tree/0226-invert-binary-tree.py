# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # simple recursive dfs
        # 
        def dfs(node):
            if node is None:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            # swap each leaf node's childs (none)
            # and recursively swap the parents above
            node.left, node.right = right, left
            return node
        
        return dfs(root)