# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return []
        
        # use defaultdict to maintain
        # index -> node.val
        res = defaultdict(list)
        q = deque([(root, 0)])
        min_lvl = 0
        max_lvl = 0
        while q:
            # simple BFS with a twist
            # at each node, if left subnode exists
            # subtract curr_lvl to get min_index
            # do this to get the leftmost index
            # we dont care about the horizontal size of the tree
            # a node at a lvl/index goes in the same defaultdict's list/value
            for _ in range(len(q)):
                ele, curr_lvl = q.popleft()
                
                res[curr_lvl].append(ele.val)
                
                min_lvl = min(min_lvl, curr_lvl)
                max_lvl = max(max_lvl, curr_lvl)
                
                if ele.left:
                    q.append((ele.left, curr_lvl - 1))
                if ele.right:
                    q.append((ele.right, curr_lvl + 1))
        
        # iterate over the list to create a new list
        # from min_val to max_val (smallest to largest index)
        return [res[i] for i in range(min_lvl, max_lvl + 1)]