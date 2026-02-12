# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # use stack for LIFO
        res = []
        stack = [(root, 0)]
        # maintain a lvl variable to track
        # which height we are at 
        lvl = -1
        while stack:
            # pop the rightmost variable first
            node, curr_lvl = stack.pop()
            if node is not None:
                # add child nodes with lvl + 1
                stack.append((node.left, curr_lvl+1))
                stack.append((node.right, curr_lvl+1))
                # if nodes in this level have not been touched
                # add the right most node and update lvl
                if curr_lvl > lvl:
                    res.append(node.val)
                    lvl = curr_lvl
        return res