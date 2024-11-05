class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import Counter, defaultdict
        graph, in_edges = defaultdict(list), defaultdict(list)
        for i in range(0,numCourses):
            in_edges[i] = 0
        for dest,pre in prerequisites:
            graph[pre].append(dest)
            in_edges[dest] +=1 
        
        queue = [item for item in range(numCourses) if in_edges[item] == 0]
        ans = []
        while queue:
            stack = queue.pop(0)
            ans.append(stack)
            children = graph[stack]
            for cur in children:
                in_edges[cur] -=1
                if in_edges[cur] == 0:
                    queue.append(cur)
        return len(ans) == numCourses