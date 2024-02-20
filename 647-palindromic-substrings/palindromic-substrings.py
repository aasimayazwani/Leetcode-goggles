class Solution:
    def countSubstrings(self, s: str) -> int:
        counting = 0
        for length in range(0,len(s)):
            current = s[0:length]
            for index in range(length,len(s)):
                current += s[index]
                #print(current)
                if current == current[::-1]:
                    counting +=1
                current = current[1:]

        return counting