class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def backtrack(current,n,left,right):
            if (left == n) and (right == n):
                ans.add(current)
                return 
            if right < n:
                backtrack(current+")",n, left, right + 1)
            if left < n:
                backtrack(current+"(",n, left + 1, right)
        backtrack("",n,0,0)
        combinations = list(ans)
        result = []
        for i in range(0,len(combinations)):
            if self.check(combinations[i]) == True:
                result.append(combinations[i])
        return result

    def check(self,arr):
        arr = [item for item in arr]
        stack = []
        while len(arr):
            if len(stack) == 0:
                stack.append(arr[0])
                arr.pop(0)
            else:
                if arr[0] == ")":
                    stack.pop(-1)
                if arr[0] == "(":
                    stack.append(")")

                arr.pop(0)
        return len(stack) == 0