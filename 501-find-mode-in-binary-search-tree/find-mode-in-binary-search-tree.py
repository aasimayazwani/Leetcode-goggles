# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        value = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                value.append(root.val)
                dfs(root.right)

            return value
        from collections import Counter    
        arr = dfs(root)
        mapping = Counter(arr)
        maximum = max(list(mapping.values()))
        return [item[0] for item in mapping.items() if item[1] == maximum ]