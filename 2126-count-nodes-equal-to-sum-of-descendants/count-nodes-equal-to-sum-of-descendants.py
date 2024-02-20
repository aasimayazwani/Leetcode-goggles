# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        answer = []
        def dfs(root):
            if root == None:
                return 0
            else:
                left_sum = dfs(root.left)
                right_sum = dfs(root.right)

                if root.val == sum([left_sum,right_sum]):
                    answer.append(root.val)

                return root.val + left_sum + right_sum 

        dfs(root)
        return len(answer)