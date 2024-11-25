class MyQueue:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr = [x] + self.arr

    def pop(self) -> int:
        return self.arr.pop(-1)

    def peek(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        return len(self.arr) == 0        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()