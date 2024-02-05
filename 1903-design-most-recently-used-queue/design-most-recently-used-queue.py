class MRUQueue:

    def __init__(self, n: int):
        self.arr = list(range(1,n+1))

    def fetch(self, k: int) -> int:
        t = self.arr.pop(k-1)
        self.arr.append(t)
        return self.arr[-1]

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)