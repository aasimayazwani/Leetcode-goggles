class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # the position of the words is not relevant 
        # doesn't need to be recoreded
        # the length of theh words is the same 
        # all the words are in lowercase 
        # calculate the absolute sum of the key values present in the either of the dictionaries

        from collections import Counter
        word1dict = Counter(word1)
        word2dict = Counter(word2)

        explored = {}

        total_sum = []
        for key in word1dict:
            freq1 = word1dict[key]
            explored[key] = 1
            if key in word2dict:
                freq2 = word2dict[key]
            else:
                freq2 = 0
            total_sum.append(abs(freq1 - freq2))
        #print(total)
        for key in word2dict:
            if key not in explored:
                freq1 = word2dict[key]
                if key in word1dict:
                    freq2 = word1dict[key]
                else:
                    freq2 = 0
                total_sum.append(abs(freq1 - freq2))
            else:
                pass
        print(total_sum)
        return max(total_sum) <= 3  
