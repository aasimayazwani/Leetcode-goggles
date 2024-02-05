# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = self.get_arr(l1)
        arr2 = self.get_arr(l2)
        nums = [int(str(item)) for item in str(arr1+ arr2)][::-1]
        
        current = ListNode(0)
        temp = current
        
        for i in range(0,len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next
        return current.next

    def get_arr(self,node):
        arr = []
        while node:
            arr.append(str(node.val))
            node = node.next 
        return int("".join(arr)[::-1])

