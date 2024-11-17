# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        from string import ascii_lowercase
        words = ascii_lowercase
        mapping = {}
        for i in range(0,len(words)):
            mapping[i] = words[i]
        ans = []
        def dfs(root,path):
            if root == None:
                return 
            if root.left == None and root.right == None:
                ans.append(path+str(mapping[root.val]))
            dfs(root.left,path+str(mapping[root.val]))
            dfs(root.right,path+str(mapping[root.val]))

        dfs(root,"")
        ans = [item[::-1] for item in ans]
        heapq.heapify(ans)
        a = heapq.heappop(ans)
        return a 