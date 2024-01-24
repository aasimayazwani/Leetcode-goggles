class Solution:
    def reverseVowels(self, s: str) -> str:
        from collections import Counter
        vowels = "aeiouAEIOU"
        vowel_mapping = Counter(vowels)

        vowels_collector = []

        for i in range(0,len(s)):
            if s[i] in vowel_mapping:
                vowels_collector.append(s[i])

        answer = ""
        for i in range(0,len(s)):
            if s[i] not in vowel_mapping:
                answer += s[i]
            if s[i] in vowel_mapping:
                answer += vowels_collector[-1]
                vowels_collector.pop(-1)
        return answer 