class Solution:
    def longestCommonPrefix(self, strs):
        present = []
        S = strs
        lengths = []
        if len(strs)==0:
            return ""
        for i in range(0,len(S)):
            lengths.append(len(S[i]))
        minimum_length = min(lengths)
        ele = ""
        while minimum_length !=0:
            print(S)
            print(present)
            present = []
            for j in range(0,len(S)):
                if S[0][0] == S[j][0]:
                    present.append(True)
                else:
                    present.append(False)
            if len(set(present))==1:
                ele +=S[0][0] 
                minimum_length -=1
                for i in range(0,len(S)):
                    S[i]= S[i][1:]
            else:
                break 
        if len(ele) >= 1:
            return ele 
        else:
            return ""