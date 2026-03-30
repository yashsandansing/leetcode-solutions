# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodeList = []
        def traverse(node):
            if node is None:
                return None
            left = traverse(node.left)
            nodeList.append(node.val)
            right = traverse(node.right)
            
        traverse(root)
        def buildTree(start: int, end: int) -> Optional[TreeNode]:
            if end < start:
                return None
            mid = (start + end) // 2
            node = TreeNode(val = nodeList[mid])
            # print(node.val, start, mid, end)
            # if start == mid == end:
            #     return None
            node.left = buildTree(start, mid - 1)
            node.right = buildTree(mid + 1, end)

            return node

        print(nodeList)
        newTree = buildTree(0, len(nodeList) - 1)
        return newTree


        
        