# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # reverse 2nd half to link twins together
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        child = slow
        prev = None

        while child:
            # print('in this loop first')
            temp = child.next
            child.next = prev
            
            prev = child
            child = temp
        
        first, last = head, prev
        res = 0
        while last:
            # print('in this loop')
            res = max(res, first.val + last.val)

            first = first.next
            last = last.next


        return res