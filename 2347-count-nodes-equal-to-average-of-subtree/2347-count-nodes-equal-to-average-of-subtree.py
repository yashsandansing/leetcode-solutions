# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total_count = 0
        def dfs(node):
            nonlocal total_count
            # sum, count
            if node is None:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            sum = left[0] + node.val + right[0]
            curr_count = 1 + left[1] + right[1]

            curr_avg = sum // curr_count
            if curr_avg == node.val:
                total_count += 1
            
            return sum, curr_count
        
        dfs(root)
        return total_count