class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        consecutive_element = []
        for i in range(0,len(nums)-1):
            if nums[i] == key:
                consecutive_element.append(nums[i+1])
        from collections import Counter
        mapping = Counter(consecutive_element)
        most_frequent = max(mapping.values())
        return [item[0] for item in mapping.items() if item[1] == most_frequent][0]