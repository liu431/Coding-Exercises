# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Track visited nodes
        visited = set()
        # Go through all nodes
        while head != None:
            # Current node's reference is in the set
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
            
            
        
