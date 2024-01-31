class Solution:
    def longestCommonPrefix(self, strs): 
        if len(set(strs)) == 1:
            return strs[0]

        result = []
        minimum = min([len(item) for item in strs])
        print(minimum)
        for length in range(1,minimum+1):
            mapping = {}
            for i in range(0,len(strs)):
                current = strs[i][0:length]
                if current not in mapping:
                    mapping[current] = 1 
                
            #print(mapping)
            if len(mapping) == 1:
                result.append(list(mapping.keys())[0])
        if len(result) == 0:
            return ""
        return result[-1]
