# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root,path):
            if root == None:
                return 
            else:
                dfs(root.left,path+">"+str(root.val))
                if (root.left == None) and (root.right == None):
                    total_path = path + ">" + str(root.val)
                    values = [int(item) for item in total_path.split(">") if len(item) > 0]
                    total = sum(values)
                    if total == targetSum:
                        ans.append(values)
                dfs(root.right,path+">"+str(root.val))
                
        dfs(root,"")
        #print(ans)
        return ans