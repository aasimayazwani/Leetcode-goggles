class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ## CREATE A STACK FOR LEFT AND RIGHT FACING BRACKETS
        left = []
        left_pos = []
        right = []
        right_pos = []
        for i in range(0,len(s)):
            if s[i] == "(":
                left.append("(")
                left_pos.append(i)
            if s[i] == ")":
                if len(left) > 0:
                    left.pop(-1)
                    left_pos.pop(-1)
                else:
                    right.append(")")
                    right_pos.append(i)

        positions = left_pos + right_pos
        answer = []
        for i in range(0,len(s)):
            if i not in positions:
                answer.append(s[i])
        return "".join(answer)


            