class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        words1_dict = Counter(words1)
        words2_dict = Counter(words2)
        unique_dict1 = [item[0] for item in list(words1_dict.items()) if item[1] == 1 ]
        unique_dict2 = [item[0] for item in list(words2_dict.items()) if item[1] == 1 ]

        counting = 0
        for i in range(0,len(unique_dict1)):
            if unique_dict1[i] in unique_dict2:
                counting +=1 
        return counting