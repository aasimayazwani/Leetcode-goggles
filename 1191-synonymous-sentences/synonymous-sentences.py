from typing import List

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        sentence = text.split(" ")
                
        def find(node):
            # Path compression for Union-Find
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex, nodey):
            # Union by root
            rootX, rootY = find(nodex), find(nodey)
            if rootX != rootY:
                parent[rootY] = rootX

        parent = {}

        # Step 1: Initialize Union-Find parent structure dynamically and union synonyms
        for x, y in synonyms:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            union(x, y)

        # Step 2: Create a mapping from root to all synonyms in that group
        mapping = {}
        for word in parent:
            root = find(word)  # Ensure path compression for all words
            if root not in mapping:
                mapping[root] = []
            mapping[root].append(word)

        # Sort each list of synonyms in `mapping` for lexicographic order
        for key in mapping:
            mapping[key].sort()

        ans = []

        # Step 3: Backtracking function to generate sentences
        def backtrack(sentence, mapping, result):
            if len(sentence) == 0:
                ans.append(" ".join(result))
            else:
                current = sentence[0]
                root = find(current) if current in parent else current  # Use root if available
                if root in mapping:
                    for synonym in mapping[root]:
                        backtrack(sentence[1:], mapping, result + [synonym])
                else:
                    backtrack(sentence[1:], mapping, result + [current])

        # Start backtracking with the initial sentence
        backtrack(sentence, mapping, [])
        
        return sorted(ans)  # Sort final results lexicographically
