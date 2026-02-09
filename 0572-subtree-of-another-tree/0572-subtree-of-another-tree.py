# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def traverse(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
            else:
                return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val==subRoot.val:
                    if traverse(node, subRoot):
                        return True
                stack.append(node.left)
                stack.append(node.right)
            
        return False