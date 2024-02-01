class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(0,len(numbers)):
            if numbers[i] not in mapping:
                mapping[numbers[i]] = [i+1]
            else:
                mapping[numbers[i]].append(i+1)

        keys = list(mapping.keys())
        for i in range(0,len(keys)):
            current = keys[i]
            left = target - current
            if (left not in mapping):
                pass

            if left in mapping:
                if (left == current) and len(mapping[left])>1:
                    ans = mapping[left]
                    return [ans[0],ans[-1]]
                if (left != current):
                    return [mapping[current][0],mapping[left][0]]
                else:
                    pass 

            