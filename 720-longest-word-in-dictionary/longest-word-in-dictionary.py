class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words,key = lambda x:(len(x),x),reverse=True)
        answers = {}
        from collections import Counter
        mapping = Counter(words)
        for i in range(0,len(words)):
            if self.sliding(words[i],mapping) == True:
                if len(words[i]) not in answers:
                    answers[len(words[i])] = [words[i]]
                if len(words[i]) in answers:
                    answers[len(words[i])].append(words[i]) 
        correct = [item for item in list(answers.keys())]
        if len(correct) > 0:
            value = max(correct)
            t1 = sorted(answers[value],reverse=False)
            if len(t1) > 0:
                return t1[0]
            return ""
        else:
            return ""


    def sliding(self,words,mapping):
        current = ""
        for i in range(0,len(words)):
            current += words[i]
            #print(current)
            if current not in mapping:
                return False
            else:
                pass 
        return True


