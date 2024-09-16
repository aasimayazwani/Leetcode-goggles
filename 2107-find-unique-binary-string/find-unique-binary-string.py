class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def iterate(current, target_length):
            if len(current) == target_length:
                ans.append(current)
                return 
            elif len(current) < target_length:
                for i in ["0","1"]:
                    iterate(current + i, target_length)
        ans = []
        iterate("",len(nums))
        return [item for item in ans if item not in nums][0]
