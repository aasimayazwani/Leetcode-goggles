class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_value = 0
        for test_value in range(1,1000):
            #print(test_value)
            if len([item for item in citations if item >= test_value]) >= test_value:
                max_value = max(max_value,test_value) 
            else:
                break
        return max_value