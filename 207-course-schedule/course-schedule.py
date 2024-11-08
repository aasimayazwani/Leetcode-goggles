class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph, in_degree = defaultdict(list), [0]*numCourses

        for i in range(0,len(prerequisites)):
            dest, prev = prerequisites[i]
            graph[prev].append(dest)
            in_degree[dest] += 1

        queue = [item for item in range(numCourses) if in_degree[item] == 0]
        answer = []
        while queue:
            cur = queue.pop(0)
            answer += [cur]
            candidate = graph[cur]
            for i in range(0,len(candidate)):
                in_degree[candidate[i]] -=1 
                if in_degree[candidate[i]] == 0:
                    queue.append(candidate[i])
        return len(answer) == numCourses

