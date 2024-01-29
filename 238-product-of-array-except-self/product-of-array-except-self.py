class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        for i in range(0,len(nums)):
            product = product*nums[i]
        mapping = {}
        for i in range(0,len(nums)):
            if nums[i] == 0:
                mapping[i] = 1

        # check if the mapping dictionary has any items present
        # if the current key is not the 
        if len(mapping) == 0:
            return [int(product/item) for item in nums]
        else:
            answer = [] 
            for i in range(0,len(nums)):
                if len(mapping) > 1:
                    answer.append(0)
                if len(mapping) == 1:
                    if i in mapping:
                        c1 = 1
                        for i in range(0,len(nums)):
                            if nums[i] != 0:
                                c1 = c1*nums[i]
                        answer.append(c1)

                    else :
                        answer.append(0)
            return answer