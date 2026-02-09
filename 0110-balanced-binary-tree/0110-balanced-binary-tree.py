# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            if root is None:
                return (True, 0)
            left = traverse(root.left)
            right = traverse(root.right)
            diff = abs(left[1] - right[1])
            status =  left[0] and right[0] and diff<=1
            return (status, 1 + max(left[1], right[1]))

        return traverse(root)[0]