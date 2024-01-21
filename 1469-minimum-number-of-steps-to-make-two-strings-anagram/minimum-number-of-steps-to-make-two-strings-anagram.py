class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # length of both strings is the same 
        # the position of the items isn't relevant 
        # only concerned about the frequency of the unique elements
        from collections import Counter
        s_map = Counter(s)
        t_map = Counter(t)

        counting  = 0
        unique  =list(set(t))
        for i in range(0,len(unique)):
            if unique[i] not in t_map:
                t_map[unique[i]] = 0
            if unique[i] not in s_map:
                s_map[unique[i]] = 0 

        for i in range(0,len(unique)):
            if t_map[unique[i]] > s_map[unique[i]]:
                diff = abs(t_map[unique[i]] - s_map[unique[i]])
                counting += diff 

        return counting 