class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat_pairs = []
        for n in range(0,len(mat2[0])):
            pairs = []
            for k in range(0,len(mat2)):
                    pairs.append(mat2[k][n])
            mat_pairs.append(pairs)

        result = []
        for i in range(0,len(mat1)):
            current_result = []
            for j in range(0,len(mat_pairs)):
                current_result.append(self.something(mat1[i],mat_pairs[j]))
            result.append(current_result)
        #print(result )
        #return [[7,0,0],[-7,0,3]]
        return result 


    def something(self,arr1,arr2):
        total = 0 
        for i in range(0,len(arr1)):
            total += arr1[i]*arr2[i]
        print("total is ",total)
        return total