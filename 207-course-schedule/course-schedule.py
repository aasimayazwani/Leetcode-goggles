class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import Counter, defaultdict
        mapping = defaultdict(list)
        indegree = [0]*numCourses
        for prev, dest in prerequisites:
            mapping[prev].append(dest)
            indegree[dest] +=1 
        queue = [i for i in range(0,numCourses) if indegree[i] == 0]
        visited = set()
        while queue:
            cur = queue.pop(0)
            visited.add(cur)
            cand = mapping[cur]
            for i in range(0,len(cand)):
                indegree[cand[i]] -=1
                if indegree[cand[i]] == 0:
                    queue.append(cand[i])
        return len(visited) == numCourses
        