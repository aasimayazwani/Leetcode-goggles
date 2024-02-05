class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sorted array - (increasing order)
        # remove duplicates (at most twice )
        # in-place 
        length = len(nums)
        mapping = {}
        for i in range(0,length):
            if i == 0:
                nums.append(nums[i])
                mapping[nums[i]] = 1
            else:
                if nums[i] in mapping:
                    if mapping[nums[i]] < 2:
                        nums.append(nums[i])
                        mapping[nums[i]] +=1
                    else:
                        pass
                if nums[i] not in mapping:
                    mapping[nums[i]] = 1 
                    nums.append(nums[i])
                    
        del nums[0:length]
        return len(nums)