class Solution:
    def longestCommonPrefix(self, strs): 
        answer = ""
        max_length = min([len(item) for item in strs])
        pointer = 0
        while pointer < max_length:
            current_text = list(set([item[pointer] for item in strs]))
            pointer +=1 
            if len(current_text) == 1:
                answer += current_text[0]
            else:
                return answer
        return answer 