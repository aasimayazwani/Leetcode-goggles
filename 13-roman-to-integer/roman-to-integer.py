class Solution:
    def romanToInt(self, s: str) -> int:
        roman = ["I","V","X","L","C","D","M"]
        numbers = [1,5,10,50,100,500,1000]

        mapping = {}
        for i in range(0,len(roman)):
            mapping[roman[i]] = numbers[i]


        stack = []
        for i in range(0,len(s)):
            if s[i] in mapping:
                stack.append(mapping[s[i]])
        stack += [0]
        total = 0
        i = 0
        while i+1 < len(stack):
            if stack[i+1] <= stack[i]:
                total += stack[i]
                i +=1
            else:
                total  += stack[i+1] - stack[i]
                i +=2
            
        return total