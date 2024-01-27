class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_map = {}
        for row in grid:
            if tuple(row) in row_map:
                row_map[tuple(row)] += 1
            if tuple(row) not in row_map:
                 row_map[tuple(row)] = 1
        col_map = {}
        for i in range(0,len(grid)):
            values = []
            for j in range(0,len(grid[0])):
                values.append(grid[j][i])
            if tuple(values) in col_map:
                col_map[tuple(values)] += 1 
            if tuple(values) not in col_map:
                col_map[tuple(values)] = 1

        rows = list(row_map.keys())
        cols = list(col_map.keys())
        counting = 0 
        counting = 0 
        for i in range(0, len(rows)):
            for j in range(0, len(cols)):
                if rows[i] == cols[j]:
                    counting += row_map[rows[i]] * col_map[cols[j]]
        return counting