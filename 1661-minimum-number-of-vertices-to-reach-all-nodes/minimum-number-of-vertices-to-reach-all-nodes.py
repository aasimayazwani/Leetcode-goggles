class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]):
        from collections import defaultdict
        mapping = defaultdict(list)
        in_edges = [0]*(n)
        for i in range(0,len(edges)):
            x, y = edges[i]
            mapping[x].append(y)
            in_edges[y] += 1

        queue = [item for item in range(n) if in_edges[item] == 0]
        return queue 