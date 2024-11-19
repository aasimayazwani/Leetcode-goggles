# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent, depth = {}, {}
        parent[root.val] = None
        depth[root.val] = 1
        current = [root]
        level = 1
        while current:
            candidates = []
            level +=1
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    parent[node.left.val] = node.val
                    depth[node.left.val] = level
                    candidates.append(node.left)
                if node.right:
                    parent[node.right.val] = node.val
                    depth[node.right.val] = level
                    candidates.append(node.right)
            
            if len(current) >= 1:
                current = candidates
            else:
                break
        return (depth[x] == depth[y]) and (parent[x] != parent[y])

