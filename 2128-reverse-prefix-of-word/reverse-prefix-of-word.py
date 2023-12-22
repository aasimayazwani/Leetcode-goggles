class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = 1
        updated = ""
        status = False
        for right in range(0,len(word)):
            if word[right] == ch:
                status = True
                break
        if status == True:
            untested = word[right+1:]
            updated = ""
            while right >= left:
                updated += word[right]
                right -=1
            updated += untested
            return updated 
        else:
            return word 