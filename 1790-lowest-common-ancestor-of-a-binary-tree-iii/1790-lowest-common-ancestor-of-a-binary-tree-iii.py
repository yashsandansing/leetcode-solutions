"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # p and q could have the same parent
        # q could be p's child -> return q
        # p could be q's child -> return p
        p_par = set()
        
        while p:
            p_par.add(p)
            p = p.parent
        
        while q:
            if q in p_par:
                return q
            q = q.parent
        
