# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # handle edge cases
        if root is None:
            return TreeNode(val)
        
        def dfs(node, val):
            # if child is None and traversal is successful
            # return True
            if node is None:
                return True

            # in a valid binary tree -> only one path is valid
            # when traversing this way
            if val < node.val and dfs(node.left, val):
                node.left = TreeNode(val = val)

            # important to check val > node.val 
            # else if left == False, it adds val to right subtree
            elif val > node.val and dfs(node.right, val):
                node.right = TreeNode(val = val)

            return False
        
        dfs(root, val)
        
        return root