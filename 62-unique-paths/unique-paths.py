class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array d with all elements set to 1
        d = [[1] * n for _ in range(m)]

        # Iterate through the array, starting from (1, 1), and update each cell
        for row in range(1, n):
            for col in range(1, m):
                # Update each cell by summing the number of paths from the cell above and the cell to the left
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        # The bottom-right cell contains the number of unique paths
        return d[m - 1][n - 1]
