class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def backtrack(letters,current):
            if 0 == len(letters):
                ans.add("".join(current))
            if len(letters) > 0:
                ans.add("".join(current))
                for i in range(0,len(letters)):
                    backtrack(letters[0:i]+letters[i+1:],current+letters[i])
        backtrack(tiles,"")
        return len(ans) - 1 