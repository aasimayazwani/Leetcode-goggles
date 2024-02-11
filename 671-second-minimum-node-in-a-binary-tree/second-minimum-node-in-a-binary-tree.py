# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(root):
            if root == None:
                return []
            else:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)

            return result
        arr = dfs(root)
        from collections import Counter
        mapping = Counter(arr)
        if len(mapping) == 1:
            return -1 
        else:
            arr = sorted(mapping.keys())
            return arr[1]