class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        holder = []
        
        left = 0 
        right = len(nums) - 1 

        while left <= right:
            if left == right:
                holder.append(nums[left])
                return sum(holder)
            else:
                concat = ""
                concat = concat + str(nums[left]) + str(nums[right])
                left +=1 
                right -=1 
                holder.append(int(concat))
            

        return sum(holder)