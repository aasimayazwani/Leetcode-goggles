class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        students = set()
        for i in range(0,len(items)):
            ids, score = items[i]
            students.add(ids)
            if ids not in mapping:
                mapping[ids] = [-score]
                heapq.heapify(mapping[ids])
            else:
                heapq.heappush(mapping[ids],-score)
        result = []
        students = list(students)
        for i in range(0,len(students)):
            cur = mapping[students[i]]
            k= 5
            total = 0
            while k > 0:
                total += heapq.heappop(cur)
                k -=1 
            result.append([students[i],int(-total/5)])
        return result 
