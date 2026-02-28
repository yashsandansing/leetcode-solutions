# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # if curr_node is in nodes
        # if any node is in left and any other node is in right
        # curr node is our common ancestor
        # if left is None -> go to right
        # if right is None -> go to left
        # hash set -> to store nodes
        # O(n): TC
        # SC O(n + k): SC

        # 2. boil it down to normal LCA
        # p -> return
        # point to first element
        # for 1 to len(nodes) -> lca -> store in p
        # return p
        # TC: O(h*k) -> k = number of nodes
        # SC: O(1)
        
        def lca(node):
            if node is None or node in nodeset:
                return node
            
            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            if left:
                return left
            else:
                return right
        
        nodeset = set(nodes)
        res = lca(root)
        
        return res

