class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if length == odd, then at max one element could be odd 
        # if length == eveb, then all 0 elements could be odd
        from collections import Counter
        mapping = Counter(s)
        even_values = sum(count for count in mapping.values() if count % 2 == 0)
        odd_values = sum(count - 1 for count in mapping.values() if count % 2 != 0)

        return even_values + odd_values + (1 if len([item[0] for item in list(mapping.items()) if item[1]%2 != 0]) else 0)