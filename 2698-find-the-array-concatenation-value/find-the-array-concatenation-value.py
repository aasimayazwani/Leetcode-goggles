class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        holder = []
        left, right = 0, len(nums)-1
        while left <= right:
            if left < right:
                holder.append(int(str(nums[left])+ str(nums[right])))
                left +=1
                right -=1
            elif left == right:
                holder.append(nums[left])
                left +=1 
        return sum(holder)