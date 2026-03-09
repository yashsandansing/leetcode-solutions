# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        child = slow.next
        prev = None
        slow.next = None
        while child:
            temp = child.next
            child.next = prev
            prev = child
            child = temp
        
        first = head
        last = prev
        while last:
            first_next = first.next
            last_next = last.next

            first.next = last
            last.next = first_next

            first = first_next
            last = last_next