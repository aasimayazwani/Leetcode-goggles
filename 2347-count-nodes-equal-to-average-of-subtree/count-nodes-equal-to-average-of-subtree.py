class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        values = []
        def dfs(root,number):
            if root == None:
                return 0,0
            else:
                left_sum,count_left = dfs(root.left,number)
                right_sum,count_right = dfs(root.right,number)
                
                total = left_sum + right_sum + root.val
                counting = count_left + count_right + 1
                avg_values = int(total/counting)
                if avg_values == root.val:
                    values.append(1)
                return root.val + left_sum + right_sum, count_left + count_right + 1

        dfs(root,0)
        return len(values)