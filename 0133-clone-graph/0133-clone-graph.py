"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge cases -> node can be None
        # return copy instead of original entries

        # hashmap to create copies
        # (dict) to store
        # key -> original node
        # neighbors -> [nodes]

        # recursive function
        # for nei in neighbors: if it exists in hashmap, return
        # else create new with Node as the key
        # return hashmap.get(node)
        copy_hashmap = {None: None}
        def dfs(curr):

            if curr in copy_hashmap:
                return copy_hashmap[curr]
            copy_hashmap[curr] = Node(val = curr.val)
            copy_node = copy_hashmap[curr]
            for nei in curr.neighbors:
                copy_node.neighbors.append(dfs(nei))
            return copy_node
        
        dfs(node)
        return copy_hashmap[node]

