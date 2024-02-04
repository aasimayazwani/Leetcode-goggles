class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Each element in the stack will be [character, count] for that character
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                # Increment the count for the current character
                stack[-1][1] += 1
                # If count reaches k, remove the character from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Add new character with count 1
                stack.append([char, 1])
                
        # Reconstruct the string from the stack
        return ''.join(char * count for char, count in stack)
