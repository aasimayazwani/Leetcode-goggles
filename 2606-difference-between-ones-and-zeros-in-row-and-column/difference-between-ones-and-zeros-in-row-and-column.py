class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        from collections import Counter
        row_map = []
        col_map = []
        for i in range(0,len(grid)):
            row_map.append(Counter(grid[i]))
        for j in range(0,len(grid[0])):
            col_map.append(Counter([item[j] for item in grid]))
        
        answer = []
        for i in range(0,len(grid)):
            cur_collector = []
            for j in range(0,len(grid[i])):
                cur = row_map[i][0] + col_map[j][0] - row_map[i][1] - col_map[j][1]
                cur_collector.append(cur*(-1))
            answer.append(cur_collector)
        return answer