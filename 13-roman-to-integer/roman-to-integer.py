class Solution:
    def romanToInt(self, s: str) -> int:
        s = [item for item in s ]
        roman = ["I","V","X","L","C","D","M"]
        numer = [1,5,10,50,100,500,1000]

        mapping = {}
        for i in range(0,len(roman)):
            mapping[roman[i]] = numer[i]
        stack = []
        while len(s) > 0:
            if len(stack)  == 0:
                stack.append(mapping[s[0]])
                s.pop(0)
            else:
                if stack[-1] < mapping[s[0]]:
                    new = mapping[s[0]] - stack[-1]
                    stack.pop(-1)
                    s.pop(0)
                    stack.append(new)
                else:
                    stack.append(mapping[s[0]])
                    s.pop(0)
        return sum(stack)