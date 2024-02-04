class RecentCounter:

    def __init__(self):
        self.mapping = {}

    def ping(self, t: int) -> int:
        self.mapping[t] = 1
        start = t - 3000
        return len([item for item in self.mapping.keys() if (item >= start) and (item <= t) ])



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)