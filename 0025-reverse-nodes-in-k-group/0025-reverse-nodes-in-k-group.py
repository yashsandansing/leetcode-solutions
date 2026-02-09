# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # create a dummy node to set groupPrev to it
        # works if only one node is present in LL
        dummy = ListNode(0, head)
        node = dummy

        # groupPrev - points to the prefix i.e. after swapping
        # the element that would point to the end of the next
        # subarray OR start of the next `reversed` subarray
        groupPrev = node

        while True:

            # reduce n by 1 to get a linked list subsection
            # of size k
            n = k
            kth = groupPrev
            while kth and n>0:
                kth = kth.next
                n -= 1

            # if k is None = subarray is shorter than k => break
            if kth is None:
                break

            # the start of the next subarray (not yet reversed)
            groupNext = kth.next

            # prev -> first element in our subarray
            # curr -> initially should point to the 
            # first element in the "next" subarray (so our end is joined to the start of next)
            prev, curr = groupNext, groupPrev.next

            # run normal reverse logic -> to reverse arrays
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # tying up loose ends ->
            # groupPrev still points to what is now the end 
            # of our subarray (since it was reversed)
            # we point it to the start of the new reversed subarray
            # and update groupPrev to its end
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next
            