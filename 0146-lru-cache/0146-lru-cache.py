class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first = Node(0, 0) # start node to avoid indexing issues
        self.last = Node(0, 0) # last node to avoid same
        self.hmap = {}  # store key: Node
        self.first.next = self.last
        self.last.prev = self.first

    def remove(self, node):
        # remove node i.e. map prev's and next's pointers to each other
        # remove can be called at any position 
        node.prev.next, node.next.prev = node.next, node.prev
        
    def insert(self, node):
        # new element must be inserted near the end of
        # the linked list
        prev = self.last.prev
        prev.next = node
        self.last.prev = node

        node.prev = prev
        node.next = self.last
        
    def get(self, key: int) -> int:
        if self.hmap.get(key) is None:
            return -1
        
        node = self.hmap[key]
        self.remove(node)
        self.insert(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.hmap.get(key) is not None:
            val = self.hmap[key]
            self.remove(val)
        
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])

        if len(self.hmap) > self.capacity:
            rm = self.first.next
            self.remove(rm)
            del self.hmap[rm.key]
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)