class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        max_length = 0
        answers = 0
        left = 0
        total = {}

        for right in range(len(s)):
            total[s[right]] = total.get(s[right], 0) + 1

            while len(total) > k:
                total[s[left]] -= 1
                if total[s[left]] == 0:
                    del total[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)
            answers = max(answers, max_length)

        return answers
