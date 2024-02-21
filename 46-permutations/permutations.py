class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer =[]
        def iterate(arr,nums):
            if len(arr) == len(nums):
                answer.append(arr)
            if len(arr) < len(nums):
                for number in nums:
                    if number not in arr:
                        iterate(arr+[number],nums)
                    else:
                        pass
        iterate([],nums)
        return answer 