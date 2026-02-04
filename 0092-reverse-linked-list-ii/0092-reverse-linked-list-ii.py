# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # start at 0, add an extra node for edge cases
        # at the head
        start = 0
        root = ListNode(next = head)
        node = root

        # skip all elements before left index
        # store pre to point it's next pointer
        # towards the end later on
        while start < left:
            pre = node
            node = node.next
            start += 1
        
        # last is the node that was first in forward LL
        # and will point to the element after `right`
        last = node
        prev = None
        
        # reverse sub LL normally
        while start <= right:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            start += 1
        
        # manage next's to point correctly
        pre.next = prev
        last.next = node
        
        return root.next