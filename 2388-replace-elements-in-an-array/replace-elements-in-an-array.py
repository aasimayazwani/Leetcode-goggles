class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mapping = {}
        for i in range(0,len(nums)):
            mapping[nums[i]] = i 

        for old_value, new_value in operations:
            position = mapping[old_value]
            mapping[new_value] = position
            del mapping[old_value]

        result = [list(item) for item in  list(mapping.items())]
        return [item[0] for item in list(sorted(result,key = lambda x:x[1]))]