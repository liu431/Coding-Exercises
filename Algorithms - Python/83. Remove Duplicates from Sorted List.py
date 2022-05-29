# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty linked list
        if not head:
            return head
        
        # Pointers for current and next nodes
        after = head.next
        curr = head
        
        while after != None:
            # Compare its value to the node after it in the list
            ## When they are equal: skip the after node and point it to the next node next to after
            if curr.val == after.val:
                curr.next = after.next
                after = after.next
                
            ## When they are not equal: move both points to next
            else:
                after = after.next
                curr = curr.next
        
        return head
            
            
        
