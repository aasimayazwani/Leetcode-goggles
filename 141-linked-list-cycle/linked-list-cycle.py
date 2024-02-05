# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        
        while head != None:
            if head not in visited:
                visited[head] = 1 
            else:
                return True
            
            
            head = head.next
        return False 