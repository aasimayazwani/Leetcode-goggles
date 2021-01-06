class Solution:

    def sortArrayByParity(self, A):
        list1 = []
        list2 = []
        for i in range(0,len(A)):
            if A[i]%2 == 0 :
                list1.append(A[i]) 
        for i in range(0,len(A)):
            if A[i]%2 != 0 :
                list2.append(A[i])
        return list1 + list2