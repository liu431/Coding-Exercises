# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        while curr_node:
            # Store next node
            next_node = curr_node.next
            # Reverse
            curr_node.next = prev_node
            # Used in next iteration
            prev_node = curr_node
            # Move to next node
            curr_node = next_node
        return prev_node
