class Solution:
    def countSubstrings(self, s: str) -> int:
        counting = 0
        success = {}
        failed = {}
        for length in range(0,len(s)):
            current = s[0:length]
            for index in range(length,len(s)):
                current += s[index]
                if current in success:
                    counting +=1 
                elif current in failed:
                    pass
                else:
                    if current == current[::-1]:
                        counting +=1
                        success[current] = 1
                    else:
                        failed[current] = 1 
                current = current[1:]

        return counting