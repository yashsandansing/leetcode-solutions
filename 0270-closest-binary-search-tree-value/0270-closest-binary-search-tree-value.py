# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # node
        best = [root, abs(root.val - target)]

        while root:
            diff = abs(root.val - target)

            if diff < best[1] or (diff == best[1] and root.val < best[0].val):
                best = [root, diff]
            
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                break

        
        return best[0].val