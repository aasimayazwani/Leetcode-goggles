# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer_node = ListNode()
        arr1 = self.get_arr(list1)
        arr2 = self.get_arr(list2)
        arr = arr1 + arr2
        arr = sorted(arr)


        answer_node = ListNode(0)
        current = answer_node
        for i in range(0,len(arr)):
            answer_node.next = ListNode(arr[i])
            answer_node  = answer_node.next

        return current.next 

    def get_arr(self,current):
        array = []
        while current  != None:
            array.append(current.val)
            current = current.next
        return array