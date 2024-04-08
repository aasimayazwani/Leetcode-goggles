class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        c_map = self.get_creator_views(creators,views)
        min_heap = []
        answer = {}
        for i in range(0,len(creators)):
            heapq.heappush(min_heap,(-c_map[creators[i]],creators[i],-views[i],ids[i]))
        highest = -max(c_map.values())
        answer = []
        booked = set()
        while len(min_heap) > 0:
            a,b,c,d = heapq.heappop(min_heap)
            if (b not in booked) and a == highest:
                booked.add(b)
                answer.append([b,d])
        return answer 

    def get_creator_views(self,creators,views):
        c_id = {}
        for i in range(0,len(creators)):
            current = creators[i]
            if current not in c_id:
                c_id[current] = views[i]
            else:
                c_id[current] += views[i]
        return c_id 
