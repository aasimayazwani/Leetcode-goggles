class Solution:
    def flipAndInvertImage(self, A):
        all = []
        for i in range(0,len(A)):
            part = A[i]
            all.append((self.inverting(self.rotating(part))))
        return all
        
    def rotating(self,A):
        new = []
        for i in range(0,len(A)):
            new.insert(0,A[0])
            del A[0]
        return new

    def inverting(self,A):
        inverted= []
        for i in range(0,len(A)):
            if A[i] == 0 :
                inverted.append(1)
            if A[i] == 1 :
                inverted.append(0)
        return inverted 
            