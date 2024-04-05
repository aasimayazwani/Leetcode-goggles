class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if (target < letters[0]) or (target >= letters[-1]):
                return letters[0]
        def binary(letters,target):
            left = 0 
            right = len(letters)-1
            while left <= right:
                middle = left + (right - left)//2 
                mid = letters[middle]
                if target < mid:
                    right = middle - 1 
                if target >= mid:
                    left = middle + 1 
            return letters[left]
        return binary(letters,target)
                    