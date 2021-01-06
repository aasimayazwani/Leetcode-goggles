class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ''
        for c in address:
            if c != '.':
                s += c
            else: # c == '.':
                s += '[.]'
        return s