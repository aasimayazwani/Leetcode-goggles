class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = []
        counter = 0
        while s:
            #print("string is ",s)
            if counter % (numRows-1) == 0:
                fail_status = 1
                current_array = [item for item in s[0:numRows]]
                s  = s[numRows:] 
                matrix.append(current_array)
                counter += 1 
            else:
                current_array  = [s[0]]
                current_array = ["#"]*(numRows-1-fail_status) + current_array + ["#"]*fail_status
                s =  s[1:]
                counter += 1 
                matrix.append(current_array)
                fail_status += 1 
        #print(matrix)
        shifted = []
        for row in range(0,numRows):
            result = self.get_index(matrix,row)
            result = [item for item in result if item != "#"]
            if result != []:
                shifted.append("".join(result))
        return "".join(shifted)


    def get_index(self,matrix,current_index):
        current_array = []
        for i in range(0,len(matrix)):
            try:
                current_array.append(matrix[i][current_index])
            except :
                pass
        return current_array