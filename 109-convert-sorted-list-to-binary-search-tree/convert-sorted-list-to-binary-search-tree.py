# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        cur = head
        nums = []
        while cur:
            temp = cur.val
            heapq.heappush(nums,temp)
            cur = cur.next 
        arr = []
        while nums:
            arr.append(heapq.heappop(nums))
        def iter(left,right,nums):
            if left > right:
                return 
            mid = left + (right-left)//2 
            root = TreeNode(nums[mid])
            root.left = iter(left,mid-1,nums)
            root.right = iter(mid+1,right,nums)
            return root
        return iter(0,len(arr)-1,arr)