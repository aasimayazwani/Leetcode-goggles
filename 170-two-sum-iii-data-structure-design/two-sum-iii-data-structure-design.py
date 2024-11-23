class TwoSum:

    def __init__(self):
        self.arr  = []

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.arr.sort()

    def find(self, value: int) -> bool:
        left, right = 0, len(self.arr)-1
        while left < right:
            cur = self.arr[left] + self.arr[right]
            if cur == value:
                return True 
            elif cur < value:
                left +=1 
            elif cur > value:
                right -=1 
            
        return False

        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)