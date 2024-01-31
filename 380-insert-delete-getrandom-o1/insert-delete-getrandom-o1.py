from random import choice
class RandomizedSet:

    def __init__(self):
        self.mapping = {}
        self.hashset = set()

    def insert(self, val: int) -> bool:
        if val not in self.mapping:
            self.mapping[val] = 1
            self.hashset.add(val)
            return True 
        else:
            return False 

    def remove(self, val: int) -> bool:
        if val in self.mapping:
            del self.mapping[val]
            self.hashset.remove(val)
            return True
        else:
            return False 


    def getRandom(self) -> int:
        return choice(list(self.mapping.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()