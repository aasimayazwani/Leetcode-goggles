class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # since we make switch the position of any two strings
        # it makes no difference about the sequence
        # we just care about the presence or abscence of the number of 
        # strings quantity
        # we need to first determine what to make equal 
        # sum and take average if the number is diviable b the number of words it is arrange
        sentence = ""
        for i in range(0,len(words)):
            sentence += words[i]

        from collections import Counter
        mapping = Counter(sentence)
        unequal_words = [item[0] for item in list(mapping.items()) if item[1]%len(words) != 0]
        return len(unequal_words) == 0 