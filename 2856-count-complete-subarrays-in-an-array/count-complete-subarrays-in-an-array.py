class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        valid_arr = 0 
        length = len(set(nums))
        for left in range(0,len(nums)):
            current_nums = nums[left:]
            if len(set(current_nums)) >= length:
                current = set()
                for i in range(0,len(current_nums)):
                    current.add(current_nums[i])
                    if len(current) == length:
                        valid_arr += 1 
                    else:
                        pass
            else:
                pass 
        return valid_arr 

    def check_number_of_odd(self,arr,k):
        return len(set(arr)) == k