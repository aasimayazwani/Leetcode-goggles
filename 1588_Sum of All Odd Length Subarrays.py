class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = []
        for i in range(1,len(arr)+1):
            if i%2!= 0:
                res.extend(self.make_array(arr,i))
        return sum(res)
    
    def make_array(self,arr,length):
        temp = []
        for i in range(0,len(arr)-length+1):
            temp.extend(arr[i:i+length])
        return temp 