# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def dfs(root):
            if root == None:
                return []
            else:
                dfs(root.left)
                if (root.left == None) and (root.right != None):
                    results.append(root.right.val)
                elif (root.left != None) and (root.right == None):
                    results.append(root.left.val)
                dfs(root.right)
            return results

        return dfs(root)