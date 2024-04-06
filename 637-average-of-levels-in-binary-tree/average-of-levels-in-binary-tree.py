# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        def dfs(root,depth):
            if root.left != None:
                dfs(root.left,depth+1)
            result.append([root.val,depth])
            if root.right != None:
                dfs(root.right,depth+1)

        dfs(root,1)
        mapping = {}
        for i in range(0,len(result)):
            value, depth = result[i]
            if depth not in mapping:
                mapping[depth] = [value]
            else:
                mapping[depth].append(value)
        keys = sorted(list(mapping.keys()))
        ans = []
        for i in range(0,len(keys)):
            temp = mapping[keys[i]]
            ans.append(sum(temp)/len(temp))
        return ans 
        