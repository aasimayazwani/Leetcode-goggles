class TwoSum:

    def __init__(self):
        self.mapping = {}

    def add(self, number: int) -> None:
        if number in self.mapping:
            self.mapping[number] += 1
        if number not in self.mapping:
            self.mapping[number] = 1

    def find(self, value: int) -> bool:
        keys = list(self.mapping.keys())
        for i in range(0,len(keys)):
            left = value - keys[i]
            if (left != keys[i]) and (left in self.mapping):
                return True 
            if (left == keys[i]) and (self.mapping[left] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)