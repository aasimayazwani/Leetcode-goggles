class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        from collections import defaultdict
        mapping = defaultdict(list)
        inform_time = {}

        for i in range(0,len(manager)):
            if manager[i] != -1:
                mapping[manager[i]].append(i)
            inform_time[i] = informTime[i]

        stack = [[headID,inform_time[headID]]]
        ans = 0

        while stack:
            collect = []
            node = stack.pop(0)
            candidates, time = mapping[node[0]], node[1]
            for i in range(0,len(candidates)):
                cur_node = candidates[i]
                collect.append([cur_node,time + inform_time[candidates[i]]])
                ans = max(ans,time + inform_time[candidates[i]])
            stack.extend(collect)
            print(collect)
        return ans