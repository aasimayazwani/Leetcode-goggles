class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        pairs = {}
        for size in range(minSize, maxSize + 1):
            current = s[:size-1]
            for i in range(size-1, len(s)):
                current = current + s[i]
                if self.count(current, maxLetters):
                    if current in pairs:
                        pairs[current] += 1
                    else:
                        pairs[current] = 1
                    current = current[1:]
                else:
                    current = current[1:]

        # Check if pairs is empty before finding the max
        if not pairs:
            return 0

        return max([item[1] for item in pairs.items()])

    def count(self, string, maxLetters):
        return len(set(string)) <= maxLetters
