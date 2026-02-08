class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.first = Node(0)
        self.last = Node(0, self.first)
        self.first.next = self.last
        self.map = {}

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            prv = node.prev
            nxt = node.next

            prv.next, nxt.prev = nxt, prv

            self.map.pop(val, None)
        
    def pop_left(self):
        val = self.first.next.val
        self.pop(val)
        return val
    
    def push_right(self, val):
        node = Node(val, self.last.prev, self.last)
        node.prev.next = node
        self.last.prev = node
        self.map[val] = node
    
    def length(self):
        return len(self.map)
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_map = dict()  # key -> value
        self.count_map = defaultdict(int)  # key -> count
        self.freq_map = defaultdict(LinkedList)  # count -> linked_list
        self.least_count = 0

    def increment_counter(self, key):
        count = self.count_map.get(key, 0)
        self.count_map[key] += 1

        self.freq_map[count].pop(key)
        self.freq_map[count + 1].push_right(key)

        if count == self.least_count and self.freq_map[count].length() == 0:
            self.least_count += 1
        
    
    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1
        
        self.increment_counter(key)
        return self.value_map[key]
    
    def put(self, key: int, value: int) -> None:
        if self.value_map.get(key) is None and self.capacity == len(self.value_map):
            key_to_remove = self.freq_map[self.least_count].pop_left()
            self.value_map.pop(key_to_remove)
            self.count_map.pop(key_to_remove)

        self.value_map[key] = value
        self.increment_counter(key)
        self.least_count = min(self.least_count, self.count_map[key])

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)