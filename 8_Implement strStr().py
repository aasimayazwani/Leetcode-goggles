class Solution:
    def strStr(self, haystack, needle) -> int:
        if needle not in haystack:
            return -1 
        if needle =="" and haystack =="":
            return 0 
        else:       
            for i in range(0,len(haystack)-len(needle)+1):
                if (haystack[i:(i+len(needle))] == needle):
                    return i