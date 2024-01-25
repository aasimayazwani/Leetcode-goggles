#Logic
# keeping track of the zero and ones
# the question already has stated that the matrix could only have either 0 or 1's. 
# so just identify the maximum number of 0 in an arra and then substract them 
# from the length of the row
# keep track of the highest value for each row, so that you wouldn't have to calculate them in the end

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counting = {}
        for i in range(0,len(mat)):
            if mat[i].count(1) in counting:
                counting[mat[i].count(1)].append(i)
            if mat[i].count(1) not in counting:
                counting[mat[i].count(1)] = [i] 
        maximum_ones = max(list(counting.keys()))
        smallest = sorted(counting[maximum_ones])[0]
        return [smallest, maximum_ones]