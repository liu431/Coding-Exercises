# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # A pointer to the head of the list 
        res_tail = ListNode(0)
        # A pointer to the tail of the list
        res = res_tail
        carryover = 0
        while l1 or l2 or carryover:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            # Get 1 for next digit if the sum is over 10
            carryover, sumval = divmod(val1 + val2 + carryover, 10)
            res.next = ListNode(sumval)
            res = res.next
            # None if it reaches the tail of the linked list
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return res_tail.next
        
