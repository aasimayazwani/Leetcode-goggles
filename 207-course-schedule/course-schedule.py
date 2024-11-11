class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        in_edges,graph = [0]*numCourses, defaultdict(list)
        for dest, previous in prerequisites:
            graph[dest].append(previous)
            in_edges[previous] +=1 
        queue = [item for item in range(numCourses) if in_edges[item] == 0]
        ans = []
        while queue:
            cur = queue.pop(0)
            ans.append(cur)
            cand = graph[cur]
            for i in range(0,len(cand)):
                in_edges[cand[i]] -=1 
                if in_edges[cand[i]] == 0:
                    queue.append(cand[i])
        return len(ans) == numCourses

