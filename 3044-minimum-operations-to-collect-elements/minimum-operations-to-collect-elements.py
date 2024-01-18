class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        exploration = {}
        for i in range(1,k+1):
            exploration[i] = 1 
        
        counting = 0
        while len(list(exploration.keys())) > 0:
            #print(exploration)
            last = nums[-1]
            nums = nums[0:-1]
            counting +=1 
            if last in exploration.keys():
                del exploration[last]
            else:
                pass
        return counting 