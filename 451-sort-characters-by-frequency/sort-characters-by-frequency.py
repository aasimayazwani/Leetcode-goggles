class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        mapping = Counter(s)
        import heapq 
        current = [(-frequency,key) for key, frequency in mapping.items()]
        heapq.heapify(current)
        answer = ""
        while len(current) > 0:
            element = heapq.heappop(current)
            answer += element[1]*abs(element[0])
        print(answer)
        return answer 