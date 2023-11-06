# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        count = 0
        temp = head
        while head:
            count += 1 
            arr.append(head.val)
            head = head.next # makes sures the nodes keep on moving 
        middle = count//2 + 1  
        print(middle)
        counting = 0 
        while counting < middle-1 : #we'll stop once count = middle
            counting+=1 #until then, we increase count by one
            temp = temp.next #as we go to the next value
        return temp
