class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counting = []
        def dfs(root,maximum):
            if root == None:
                return 

            if root.val >= maximum:
                #print(root.val)
                maximum = root.val
                counting.append(1)
            dfs(root.left,maximum)
            dfs(root.right,maximum)

        dfs(root,-900000)

        return len(counting)