# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapping = {}
        cur = head
        while cur:
            value = cur.val
            if value not in mapping:
                mapping[value] = 1 
            else:
                mapping[value] +=1 
            cur = cur.next 
        ans = sorted(mapping.values())
        temp = ListNode(0)
        result = temp
        for i in range(0,len(ans)):
            sep = ListNode(ans[i])
            temp.next = sep
            temp = temp.next
        return result.next 

        