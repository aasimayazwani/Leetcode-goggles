# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        result = []
        while stack or cur:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            
            popped = stack.pop(-1)
            cur = popped.right
        return result 
