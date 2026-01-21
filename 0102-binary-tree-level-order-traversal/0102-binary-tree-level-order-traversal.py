# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        res = []
        while q:
            level_nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                if node is not None:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_nodes:
                res.append(level_nodes)
        return res
