class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import Counter
        mapping = {}
        for i in range(0,len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]].append(i)
            if nums[i] not in mapping:
                mapping[nums[i]] = [i]
        amount = Counter(nums)
        #nums = list(set(mapping.keys()))
        for i in range(0,len(nums)):
            left = target - nums[i]
            if (left == nums[i]) and (amount[left] > 1):
                return [mapping[nums[i]][0],mapping[nums[i]][1]]
            if (left == nums[i]) and (amount[left] == 1):
                pass
            if (left != nums[i]) and (left in mapping):
                return [i,mapping[left][0]]
            else:
                pass  