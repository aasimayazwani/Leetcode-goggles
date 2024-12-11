class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(nodex, nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                else:
                    parent[rooty] = rootx
                    rank[rootx] += 1

        # Initialize Union-Find
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        # Step 1: Union all connected cities
        for x, y, _ in roads:
            union(x, y)

        # Step 2: Find the root of city 1
        root1 = find(1)

        # Step 3: Find the minimum score for roads in city 1's connected component
        min_score = float("inf")
        for x, y, cost in roads:
            if find(x) == root1 or find(y) == root1:
                min_score = min(min_score, cost)

        # Return the minimum score
        return min_score
