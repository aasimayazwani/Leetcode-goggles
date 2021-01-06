class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        for i in range(0,int(len(nums)/2)):
            temp.append(nums[i])
            temp.append(nums[n+i])
        return temp