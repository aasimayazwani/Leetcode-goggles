class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Psuedocode
        # identify the frequency of all the words 
        # what ever the key is for the value pair, 
        # split them accodingly in that many pairs
        mapping = {}
        for i in range(0,len(groupSizes)):
            if groupSizes[i] in mapping:
                mapping[groupSizes[i]].append(i)

            if groupSizes[i] not in mapping:
                mapping[groupSizes[i]] = [i]

        numbers = list(set(groupSizes))
        result = []
        for i in range(0,len(numbers)):
            result.extend(self.split_into_subarrays(mapping[numbers[i]],numbers[i]))
        return result


    def split_into_subarrays(self,arr,length):
        result = []
        while arr:
            result.append(arr[0:length])
            arr = arr[length:]
        return result
