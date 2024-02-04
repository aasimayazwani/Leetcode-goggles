class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mapping = {k: v for k, v in knowledge}
        
        result = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1  # Skip the '('
                key_start = i
                while s[i] != ')':
                    i += 1
                key = s[key_start:i]  # Extract key
                # Append the value if the key exists, else append "?"
                result += mapping.get(key, "?")
            else:
                result += s[i]  # Directly append characters outside brackets
            i += 1  # Move to the next character

        return result