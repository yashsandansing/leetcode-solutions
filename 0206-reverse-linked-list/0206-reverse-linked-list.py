# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # next_ = None
        curr = head
        while curr: #5
            next_ = curr.next # None
            curr.next = prev # 54321

            prev=curr # 4321
            curr=next_ # 5None
        return prev

