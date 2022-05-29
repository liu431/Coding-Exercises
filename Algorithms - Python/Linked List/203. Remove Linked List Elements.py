# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        listnode = ListNode(0)
        listnode.next = head
        
        prev, curr = listnode, head
        while curr:
            if curr.val == val:
                # Set pointer to point to the node next to the one to skip
                prev.next = curr.next
            else:
                # Move pointer to the next node
                prev = curr
            curr = curr.next
            
        return listnode.next
        
