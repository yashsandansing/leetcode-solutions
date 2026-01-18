# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode()
        res = node

        node1 = l1
        node2 = l2
        
        carry = 0

        while node1 and node2:
            curr_sum = node1.val + node2.val + carry
            
            carry, val = divmod(curr_sum, 10)
            res.next = ListNode(val = val)

            res = res.next
            node1 = node1.next
            node2 = node2.next

        while node1:
            curr_sum = node1.val + carry
            carry, val = divmod(curr_sum, 10)
            res.next = ListNode(val = val)

            res = res.next
            node1 = node1.next
        
        while node2:
            curr_sum = node2.val + carry
            carry, val = divmod(curr_sum, 10)
            res.next = ListNode(val = val)

            res = res.next
            node2 = node2.next
        
        if carry>0:
            res.next = ListNode(val = carry)
        return node.next