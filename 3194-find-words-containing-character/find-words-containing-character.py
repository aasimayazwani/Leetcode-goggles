class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        positions = []
        for i in range(0,len(words)):
            current = self.find_x(words[i],x)
            if current != -1:
                positions.append(i)
        return positions

    def find_x(self,nums,character):
        for i in range(0,len(nums)):
            if nums[i] == character:
                return i
        return -1