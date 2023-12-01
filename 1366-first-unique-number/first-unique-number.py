class FirstUnique:

    def __init__(self, nums: List[int]):
        self.mapping = {}
        self.unique = {}
        self.get_mapping(nums)
        

    def showFirstUnique(self) -> int:
        try:
            return list(self.unique.keys())[0]
        except:
            return -1 

    def add(self, value: int) -> None:
        if value in self.mapping:
            self.mapping[value] +=1 
            if value in self.unique:
                del self.unique[value]
            else:
                pass 

        if value not in self.mapping:
            self.mapping[value] = 1 
            self.unique[value] = 1 
        
        
    def get_mapping(self,arr):
        for i in range(0,len(arr)):
            #print(self.unique)
            if arr[i] in self.mapping:
                self.mapping[arr[i]] +=1 
                if arr[i] in self.unique: 
                    del self.unique[arr[i]]
                else :
                    pass

            if arr[i] not in self.mapping:
                self.mapping[arr[i]] = 1 
                self.unique[arr[i]] = 1 
            



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)