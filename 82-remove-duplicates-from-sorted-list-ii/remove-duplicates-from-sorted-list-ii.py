# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import Counter
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        mapping = Counter(nums)
        current = ListNode(0)
        temp = current
        nums = [item[0] for item in mapping.items() if item[1] == 1]
        for i in range(0,len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next
        return current.next 