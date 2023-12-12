class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix_sum = [0]
        total = 0
        for i in range(0,len(arr)):
            total = total + arr[i]
            prefix_sum.append(total)
        count = 0 
        for j in range(k,len(prefix_sum)):
            current_sum = prefix_sum[j] - prefix_sum[j-k]
            average = (current_sum)/k
            if average >= threshold:
                count +=1 
                
        return count