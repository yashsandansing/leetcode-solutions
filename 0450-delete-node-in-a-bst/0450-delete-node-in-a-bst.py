# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(val = float('inf'), left = root)
        node = dummy

        while node:
            if key < node.val:
                if node.left is None:
                    break
                if node.left.val == key:
                    node.left = self.rebalance(node.left)
                    break
                node = node.left

            elif key > node.val:
                if node.right is None:
                    break
                if node.right.val == key:
                    node.right = self.rebalance(node.right)
                    break
                node = node.right

        return dummy.left

    def rebalance(self, node):
        if node.right is None:
            return node.left
        if node.left is None:
            return node.right
        
        base = node.right
        temp = node.left
        curr = base
        while curr.left is not None:
            curr = curr.left
        curr.left = temp
        return base