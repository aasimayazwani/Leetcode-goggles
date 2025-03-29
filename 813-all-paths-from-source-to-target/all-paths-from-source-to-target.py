class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        mapping = {}
        for i in range(0,len(graph)):
            mapping[i] = graph[i]
        
        def recurse(i,current):
            if i == len(graph)-1:
                ans.append(current)
                return 
            options = mapping[i]
            for i in range(0,len(options)):
                recurse(options[i],current+[options[i]])
        ans = []
        recurse(0,[0])
        return ans
