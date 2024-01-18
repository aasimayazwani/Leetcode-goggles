class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        import math
        diagonals = []
        lr = []
        for i in range(0, len(grid)):
            cur = grid[i][i]
            if cur == 0:
                return False 
            else:
                lr.append(cur)

        rl = []
        for i in range(0, len(grid)):
            cur = grid[i][len(grid) - i - 1]
            if cur == 0:
                return False
            rl.append(cur)

        if len(grid) % 2 == 0:
            for i in range(0, len(grid)):
                if sum(grid[i]) != rl[i] + lr[i]:
                    return False 
        else:  # This replaces 'if len(grid) % 2 != 0'
            middle = math.ceil(len(grid) / 2) - 1  # Corrected the calculation of middle index
            for i in range(0, len(grid)):
                if i != middle:
                    if sum(grid[i]) != rl[i] + lr[i]:
                        return False 
                else:
                    if sum(grid[i]) != rl[i]:
                        return False 
        return True