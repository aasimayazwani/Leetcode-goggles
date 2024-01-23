class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for character in s:
            if len(stack) > 0 and (stack[-1] ==  character):
                stack.pop(-1)
            else :
                stack.append(character)
        return "".join(stack)
                