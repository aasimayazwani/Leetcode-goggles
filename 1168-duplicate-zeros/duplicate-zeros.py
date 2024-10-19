class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        for i in range(0,length):
            if arr[i] == 0:
                arr.append(arr[i])
                arr.append(0)
            else:
                arr.append(arr[i])
        del arr[0:length]
        del arr[length:]
        
            
        