class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = []
        def back(nums,cur):
            if len(nums) == 0:
                ans.append(sorted(cur))
            else:
                ans.append(cur)
                for i in range(0,len(nums)):
                    back(nums[i+1:],cur+[nums[i]])
        back(nums,[])

        hashing = {}
        for item in ans:
            value = self.count_or(item)
            if value not in hashing:
                hashing[value] = [item]
            else:
                hashing[value].append(item)
                
        total = max(list(hashing.keys()))
        return len(hashing[total])

    def count_or(self,arr):
        total = 0
        for i in range(0,len(arr)):
            total |= arr[i]
        return total
