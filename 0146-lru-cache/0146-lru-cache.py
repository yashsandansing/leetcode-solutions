class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = Node(-1, -1)
        self.last = Node(-1, -1)
        self.first.next = self.last
        self.last.prev = self.first
    
    def pop(self, node: 'Node') -> None:
        prv, nxt = node.prev, node.next

        prv.next = nxt
        nxt.prev = prv
    
    def pop_left(self):
        lru_node = self.first.next
        self.pop(lru_node)
        return lru_node
    
    def push_right(self, key: int, value: int) -> 'Node':
        last = self.last
        sec_last = self.last.prev
        new_node = Node(key, value, prev = sec_last, next = last)
        last.prev = new_node
        sec_last.next = new_node

        return new_node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_map = dict()  # key: Node
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.lru_map:
            return -1
        
        node = self.lru_map[key]

        self.linked_list.pop(node)
        new_node = self.linked_list.push_right(key, node.val)
        self.lru_map[key] = new_node

        return new_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru_map:
            self.linked_list.pop(self.lru_map[key])
            del self.lru_map[key]
        
        new_node = self.linked_list.push_right(key, value)
        self.lru_map[key] = new_node

        if len(self.lru_map) > self.capacity:
            lru_node = self.linked_list.pop_left()
            del self.lru_map[lru_node.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)