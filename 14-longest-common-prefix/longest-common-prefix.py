class Solution:
    def longestCommonPrefix(self, strs): 
        answer = ""
        minimum = min([len(item) for item in strs])
        for i in range(0,minimum):
            array = [item[i] for item in strs]
            if (len(set(array)) == 1) and (len(array[0]) > 0):
                answer += array[0]
            else:
                break
        return answer 