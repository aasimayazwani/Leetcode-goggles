class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        answer = {}
        for i in range(0,len(dictionary)):
            current = dictionary[i]
            if self.get(current,s):
                length = len(current)
                if length not in answer:
                    answer[length] = [current]
                else:
                    answer[length].append(current)
        if len(answer) != 0:
            longest_words = answer[max(answer.keys())]
            return sorted(longest_words)[0]
        return ""
        
    def get(self,full,word):
        full = [item for item in full]
        word = [item for item in word]
        left, right = 0, len(word)-1
        while len(full) > 0 and left <= right:
            if word[left] == full[0]:
                full.pop(0)
                left +=1
            if len(full) > 0 and word[right] == full[-1]:
                full.pop(-1)
                right -=1
            if len(full) > 0 and word[left] != full[0]:
                left +=1
            if len(full) > 0 and word[right] != full[-1]:
                right -=1
        if len(full) == 0:
            return True
        return False