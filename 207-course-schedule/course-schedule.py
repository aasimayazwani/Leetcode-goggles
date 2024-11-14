class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict 
        graph, in_edges = defaultdict(list), [0]*numCourses
        for prev, dest in prerequisites:
            in_edges[dest] +=1 
            graph[prev].append(dest)
        queue = [item for item in range(numCourses) if in_edges[item] == 0 ]
        visited = set()
        while queue:
            cur = queue.pop(0)
            visited.add(cur)
            cand = graph[cur]
            for i in range(0,len(cand)):
                in_edges[cand[i]] -=1 

                if in_edges[cand[i]] == 0:
                    queue.append(cand[i])
        return len(visited) == numCourses
        