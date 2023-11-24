class TicTacToe:

    def __init__(self, n: int):
        self.matrix = [[-999] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        #row, col, value = item[0], item[1], item[2]
        matrix = self.set_value(row,col,player,self.matrix)
        #print(matrix)
        result1 = self.perform_diagonals_check(matrix)
        result2 = self.perform_horizontal_check(matrix)
        result3 = self.perform_vertical_check(matrix)
        winner_status = [item[1] for item in [result1,result2,result3] if item[0] == True ]
        if len(winner_status) == 0:
            return 0
        else:
            return winner_status[0]

    def set_value(self,row,col,value,matrix):
        self.matrix[row][col] = value
        return self.matrix


    def perform_diagonals_check(self,matrix):
        diagonal_1 = []
        diagonal_2 = []
        for i in range(0,len(matrix)):
            diagonal_1.append(matrix[i][i])
            diagonal_2.append(matrix[len(matrix)-i - 1][i])
        diagonals = [diagonal_1,diagonal_2]
        vertical_status, value = self.perform_horizontal_check(diagonals)
        return vertical_status, value


    def perform_horizontal_check(self,matrix):
      for i in range(0,len(matrix)):
        status, value = self.check_unique(matrix[i])
        if status == True:
                return True, value 
        else:
                pass 
      return False, -999

    def perform_vertical_check(self,matrix):
        agg_arr = []
        for j in range(0,len(matrix[0])):
            current_arr = []
            for i in range(0,len(matrix)):
                current_arr.append(matrix[i][j])
            agg_arr.append(current_arr)
        
        vertical_status, value = self.perform_horizontal_check(agg_arr)
        return vertical_status, value



    def check_unique(self,arr):
        arr = set(arr)
        if len(arr) == 1 and -999 not in arr:
            return True, list(arr)[0]
        else:
            return False, -999

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)