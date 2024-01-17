class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # CHECK ROYAL FLUSH 
        from collections import Counter

        if len(list(set(suits))) == 1:
            return "Flush"
        
        mapping = list(Counter(ranks).items())
        value = [item[0] for item in mapping if item[1] >= 3] 
        if len(value) > 0:
            return "Three of a Kind"

        second_value = [item[0] for item in mapping if item[1] >= 2] 
        if len(second_value) > 0 :
            return "Pair"

        return "High Card"