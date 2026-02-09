# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while True:
            smallest = [0, float('inf')]
            empty = True
            for ind, ll in enumerate(lists):
                if ll is not None:
                    if ll.val<smallest[1]:
                        smallest = ind, ll.val
                    empty = False
            if empty == True:
                break
            next_node = lists[smallest[0]]
            lists[smallest[0]] = next_node.next
            
            node.next = next_node
            node = node.next            
        return head.next