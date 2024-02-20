class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater_than = []
        less_than = []
        self_value = 0
        for i in range(0,len(nums)):
            if nums[i] > pivot:
                greater_than.append(nums[i])
            if nums[i] < pivot:
                less_than.append(nums[i]) 
            if nums[i] == pivot:
                self_value +=1 

        return less_than + [pivot]*self_value + greater_than
