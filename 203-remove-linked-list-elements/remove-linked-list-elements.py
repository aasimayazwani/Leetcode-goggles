# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel_node = ListNode(0)
        sentinel_node.next = head 

        previous, current = sentinel_node, head 

        while current:
            if current.val == val:
                previous.next = current.next 

            else:
                previous = previous.next 

            current =  current.next 
        return sentinel_node.next 
            
