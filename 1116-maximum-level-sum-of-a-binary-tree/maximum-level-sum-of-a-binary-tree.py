class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = {}

        def dfs(root,depth):
            if root == None:
                return 
            dfs(root.left,depth+1)
            if depth not in level_sum:
                level_sum[depth] = root.val
            else:
                level_sum[depth] += root.val
            dfs(root.right,depth+1)

        dfs(root,0)
        ans = []
        res = list(level_sum.items())      
        for i in range(0,len(res)):
            heapq.heappush(ans,(-res[i][1],res[i][0]))    
        a, b = heapq.heappop(ans)
        return b +1
