# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        mapping = {}

        def dfs(root,total,path):
            if root == None:
                return 
            dfs(root.left,total+root.val,path+">"+str(root.val))
            if root.left == None and root.right == None:
                num = total+root.val
                path = path +">"+str(root.val)
                if num not in mapping:
                    mapping[num] = [path]
                else:
                    mapping[num].append(path)

            dfs(root.right,total+root.val,path+">"+str(root.val))

        dfs(root,0,"0")
        if targetSum not in mapping:
            return []
        ans = mapping[targetSum]
        ans = [[int(item) for item in item.split(">")][1:] for item in ans]
        return ans