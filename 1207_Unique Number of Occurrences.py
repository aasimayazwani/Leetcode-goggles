class Solution:
    def uniqueOccurrences(self, arr):
        counting = []
        for i in range(0,len(list(set(arr)))):
            counting.append(arr.count(list(set(arr))[i]))
        print(counting)
        return len(list(set(counting)))==len(list(set(arr)))