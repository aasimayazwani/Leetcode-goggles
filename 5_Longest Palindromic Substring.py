class Solution:
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        else:
            for i in reversed(range(1,len(s)+1)):
                print(i)
                if self.main(s,i) != None:
                    return self.main(s,i)
            return ""

    def main(self,arr,length): 
        for i in range(0,len(arr)-length+1):
            val = arr[i:i+length]
            if val[::-1] == val:
                return val
        return None