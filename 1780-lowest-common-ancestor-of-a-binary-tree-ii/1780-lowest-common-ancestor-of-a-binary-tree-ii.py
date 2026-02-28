# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if node == p or node == q or node is None:
                return node
            
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)

            if left and right:
                return node
            if left:
                return left
            else:
                return right
        
        result = lca(root, p, q)
        # result could be None
        if result != p and result != q:
            return result
        
        if (result == p and lca(root, q, q) == None) or (result == q and lca(root, p, p) == None):
            return None
        return result