class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_dict = self.dictionary(nums)
        keys = list(num_dict.keys())
        for i in range(0,len(keys)):
            if self.checking_search(num_dict[keys[i]],k):
                return True
        return False  
    
    
    def dictionary(self,integers):
        numbers = dict()
        for i in range(0,len(integers)):
            if integers[i] not in numbers:
                numbers[integers[i]] = [i] 
            else:
                numbers[integers[i]].append(i)
        return numbers

    def checking_search(self,arr,k):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i!= j:
                    if abs(arr[i] - arr[j])<= k:
                        return True 
        return False 
        