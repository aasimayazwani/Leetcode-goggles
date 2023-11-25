class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## checking each row and each column 
        ## and checking each block 
        # create a universal function to identify duplicates in a array 
        # loop through each row return false in case duplicate found and return the ame and the process ends. 
        result = set([self.checking_row(board),self.checking_column(board),self.checking_grid(board)])
        #print(result)
        if False in result:
            return False
        return True  


    def checking_grid(self,board):
        positions = [[0,1,2],[3,4,5],[6,7,8]]
        agg = []
        for col in range(0,len(positions)):
            for current_positions in positions:
                    current_blocks = []
                    for row in current_positions:
                        current = board[row][positions[col][0]:positions[col][-1]+1]
                        current_blocks.append(current)
                    agg.append(current_blocks)
        for i in range(0,len(agg)):
            current_a = sum(agg[i],[])
            if self.checking_array(current_a) == False:
                return False 
            else :
                pass
        return True


    def checking_row(self,board):
        for i in range(0,len(board)):
            current_row = board[i]
            if self.checking_array(current_row) == False:
                return False 
            else :
                pass 
        return True

    def checking_column(self,board):
        agg_arr = []
        for column in range(0,len(board[0])):
            current_array = []
            for row in range(0,len(board)):
                current_array.append(board[row][column])
            #print(current_array)
            if self.checking_array(current_array) == False:
                return False 
            else :
                pass
        return True


    def checking_array(self,arr):
        arr = [item for item in arr if item != "."]
        nums = set()
        for i in range(0,len(arr)):
            if arr[i] != ".":
                if arr[i] in nums:
                    #print(arr[i])
                    return False 
                if arr[i] not in nums:
                    nums.add(arr[i])
            else :
                pass
        return True
