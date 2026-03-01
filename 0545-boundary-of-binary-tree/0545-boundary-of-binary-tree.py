# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_nodes = self.left_dfs(root.left)
        right_nodes = self.right_dfs(root.right)
        leaf_nodes = self.get_leaf_nodes(root.left) + self.get_leaf_nodes(root.right)

        return [root.val] + left_nodes + leaf_nodes + right_nodes[::-1]

    def left_dfs(self, node):
        
        if node is None or (node.left is None and node.right is None):
            return []
        if node.left:
            return [node.val] + self.left_dfs(node.left)
        else:
            return [node.val] + self.left_dfs(node.right)

    def right_dfs(self, node):
        if node is None or (node.left is None and node.right is None):
            return []
        if node.right:
            return [node.val] + self.right_dfs(node.right)
        else:
            return [node.val] + self.right_dfs(node.left)

    def get_leaf_nodes(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.get_leaf_nodes(node.left) + self.get_leaf_nodes(node.right)