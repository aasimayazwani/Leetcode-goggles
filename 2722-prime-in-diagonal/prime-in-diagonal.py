class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        size=len(nums)
        max=0
        for i in range(size):
            if self.isPrime(nums[i][i]) and max<nums[i][i]:
                max=nums[i][i]
            if self.isPrime(nums[i][size- i - 1]) and max<nums[i][size- i - 1]:
                max=nums[i][size- i - 1]
        return max

    def isPrime(self,n:int) -> bool:
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i=i+1
        return True