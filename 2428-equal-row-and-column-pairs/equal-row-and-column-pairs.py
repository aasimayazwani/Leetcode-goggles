class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        explored_rows = {}
        
        for i in range(0,len(grid)) :
            explored_rows[str(i)] = grid[i]

        number_of_columns = len(grid[0])
        counting = 0

        for i in range(0,number_of_columns):
            current_columns = [item[i] for item in grid]
            counting += self.check_matching(current_columns,explored_rows)
        return counting
            
    def check_matching(self,column,explored_rows):
        count = 0
        keys = list(explored_rows.keys())
        for i in range(0,len(keys)):
            if explored_rows[keys[i]] == column:
                count +=1 
            else :
                pass 
        return count