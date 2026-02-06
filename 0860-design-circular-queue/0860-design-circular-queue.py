class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# use a linked list to store node(s)
# current and next and index (position in linked list)

class MyCircularQueue:

    def __init__(self, k: int):
        self.root = Node(val = -1, next = None)
        self.limit = k

    def enQueue(self, value: int) -> bool:
        node = self.root
        curr_idx = 0
        while node.next is not None:
            node = node.next
            curr_idx += 1
        
        if curr_idx == self.limit:
            return False
        
        node.next = Node(val = value)
        return True

    def deQueue(self) -> bool:
        node = self.root
        if node.next is not None:
            node.next = node.next.next
            return True
        return False

    def Front(self) -> int:
        node = self.root
        return node.next.val if node.next is not None else -1

    def Rear(self) -> int:
        node = self.root
        while node.next is not None:
            node = node.next
        return node.val

    def isEmpty(self) -> bool:
        node = self.root
        return False if node.next is not None else True

    def isFull(self) -> bool:
        node = self.root
        curr_idx = 0
        while node.next is not None:
            node = node.next
            curr_idx += 1
        
        if curr_idx == self.limit:
            return True
        return False        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()