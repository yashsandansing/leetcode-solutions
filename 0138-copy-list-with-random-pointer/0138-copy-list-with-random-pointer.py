"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        clone_map = {None: None}
        q = deque()
        
        q.append(head)
        clone_map[head] = Node(head.val)

        while q:
            node = q.popleft()
            node_ref = clone_map[node]

            if node.next not in clone_map:
                clone_map[node.next] = Node(node.next.val)
                q.append(node.next)
            
            node_ref.next = clone_map[node.next]

            if node.random not in clone_map:
                clone_map[node.random] = Node(node.random.val)
                q.append(node.random)

            node_ref.random = clone_map[node.random]

        
        return clone_map[head]