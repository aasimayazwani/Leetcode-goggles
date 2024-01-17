class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # array of arrays
        # elements of the array are all positive
        # all elements present in the arrays are unique
        # find the common elements present in all the arrys 
        # the amout and the position of the elements is not relevant

        from collections import Counter
        collections = [Counter(item) for item in nums]
        answers = []
        current = collections[0]
        comparitive = collections[0:]
        for key in current.keys():
            counting = 0
            for mapping in comparitive:      
                if key not in mapping:
                    break
                if key in mapping:
                    counting +=1
            if counting == len(comparitive):
                answers.append(key)
        return sorted(answers)
        
            
        