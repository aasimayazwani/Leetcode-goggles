# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        answer = []
        def dfs(root,depth):
            if root == None:
                return 
            else:
                dfs(root.left,depth+1)
                if root.left == None and root.right == None:
                    answer.append([root.val,depth])
                dfs(root.right,depth+1)

        dfs(root,1)
        #print(answer)
        max_depth = max([item[1] for item in answer])
        return sum([item[0] for item in answer if item[1] == max_depth])