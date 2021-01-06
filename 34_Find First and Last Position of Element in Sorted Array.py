class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<1:
            return [-1,-1]
        
        index = self.BinarySearch(nums,target)
        
        if index != -1:
            left_values = self.left_searching(nums,index,target)
            right_values = self.right_searching(nums,index,target)
            trends =  left_values + right_values + [index] 
            #print(trends)
            output = set()
            for x in trends:
                output.add(x)
            if len(output) ==1:
                return [list(output)[0],list(output)[0]]
            else:
                return [min(output),max(output)]
        
        else:
            return[-1,-1]
        
    def BinarySearch(self, combined_array,target):
        initial = 0 
        final = len(combined_array)-1
        while initial <= final :
            middle_element = (initial + final)//2
            if combined_array[middle_element] > target:
                final = middle_element-1 
            if combined_array[middle_element] < target:
                initial = middle_element +1   
            if combined_array[middle_element] == target:
                return middle_element
        return -1 
    
    def left_searching(self,array,index,item):
        listing = []
        while index>=0 and array[index] == item:
            listing.append(index)
            index-=1
        return listing
    
    def right_searching(self,array,index,item):
            listing = []
            while index< len(array) and array[index] == item:
                listing.append(index)
                index+=1
            return listing