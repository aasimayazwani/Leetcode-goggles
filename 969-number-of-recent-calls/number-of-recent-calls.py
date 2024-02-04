from collections import deque

class RecentCounter:

    def __init__(self):
        self.mapping = deque()

    def ping(self, t: int) -> int:
        self.mapping.append(t)
        pointer = 0 
        while len(self.mapping) > 0:
            if self.mapping[0] < t - 3000:
                self.mapping.popleft()
                pointer +=1 
            else:
                break

        return len(self.mapping)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)