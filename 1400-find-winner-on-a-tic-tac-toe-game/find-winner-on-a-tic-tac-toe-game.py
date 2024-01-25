class Solution:
    def tictactoe(self, moves):
        collection = []
        for i in range(0,3):
            arr = []
            for j in range(0,3):
                arr.append(0)
            collection.append(arr)
        
        for i in range(0,len(moves)):
            if i%2 == 0:
                collection[moves[i][0]][moves[i][1]]  = "X"
            else:
                collection[moves[i][0]][moves[i][1]]  = "O"
                
        row_collection = [] 
        for i in range(0,len(collection)):
            row_collection.append(collection[i])
        
        column_collection = []
        for i in range(0,len(collection)):
            nums  = []
            for j in range(0,len(collection)):
                nums.append(collection[j][i])
            column_collection.append(nums)
        #print(column_collection)


        lr_diagonal = []
        for i in range(0,len(collection)):
            lr_diagonal.append(collection[i][i])

        rl_diagonal = []
        for i in range(0,len(collection)):
            rl_diagonal.append(collection[i][len(collection[0]) - i-1])
        
        answer = [rl_diagonal] + [lr_diagonal] + row_collection + column_collection    
        for i in range(0,len(answer)):
            if (len(set(answer[i])) ==1) and (answer[i][0] == "X"):
                return "A"
            if (len(set(answer[i])) ==1) and (answer[i][0] == "O"):
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"