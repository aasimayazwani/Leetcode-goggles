# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        mapping = {}
        mapping["x"] = -1
        mapping["y"]=-2
        parent_map= {}
        parent_map["x"]= -1
        parent_map["y"]=-2

        def dfs(root,parent,depth):
            if root == None:
                return 
            else:
                dfs(root.left,root,depth+1)
                dfs(root.right,root,depth+1)
                if root.val == x:
                    mapping["x"] = depth 
                    parent_map["x"] = parent.val if parent else None
                if root.val == y:
                    mapping["y"] = depth 
                    parent_map["y"] = parent.val if parent else None
 

        dfs(root,None,0)
        #print(parent_map)
        return mapping["x"] == mapping["y"]   and parent_map["x"]!= parent_map["y"]