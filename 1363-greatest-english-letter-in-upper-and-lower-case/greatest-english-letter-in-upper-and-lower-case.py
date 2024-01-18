class Solution:
    def greatestLetter(self, s: str) -> str:
        from collections import Counter
        mapping = Counter(s)
        
        s = sorted(s.lower())
        answers = []
        for i in range(0,len(s)):
            if (s[i].upper() in mapping) and (s[i] in mapping):
                answers.append(s[i].upper())
        if len(answers) > 0:
            return answers[-1]
        else:
            return ""
