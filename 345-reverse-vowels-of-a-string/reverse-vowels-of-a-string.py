class Solution:
    def reverseVowels(self, s: str) -> str:
        from collections import Counter
        vowels = "aeiouAEIOU"
        mapping = Counter(vowels)
        nums = [item for item in s]
        left = 0
        right = len(s)-1
        while left < right:
            if nums[left] in mapping and nums[right] in mapping:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 
                right -=1 
            else:
                if nums[left] not in mapping and nums[right] in mapping:
                    left +=1 
                if nums[left] in mapping and nums[right] not in mapping:
                    right -=1 
                if nums[left] not in mapping and nums[right] not in mapping:
                    left +=1 
                    right -=1 
        return "".join(nums)
                