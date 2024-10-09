# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        current = head
        while current.next is not None:
            if current.val != current.next.val:
                current = current.next 
            else:
                current.next = current.next.next
        return head 