class Solution:
    def findRLEArray(self, encoded1, encoded2):
        # Initialize pointers and the result array
        i, j = 0, 0
        result = []

        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            # Multiply the values and take the minimum of the frequencies
            product = val1 * val2
            min_freq = min(freq1, freq2)
            encoded1[i][1] -= min_freq
            encoded2[j][1] -= min_freq

            # Add/merge to result
            if result and result[-1][0] == product:
                result[-1][1] += min_freq
            else:
                result.append([product, min_freq])

            # Move the pointers
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return result
