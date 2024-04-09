class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        mapping = []
        num = [item for item in str(num)]
        for i in range(0,len(num)):
            if int(num[i])%2 == 0:
                heappush(even,-int(num[i]))
                mapping.append("even")
            if int(num[i])%2 != 0:
                heappush(odd,-int(num[i])) 
                mapping.append("odd")
        result = ""
        for i in range(0,len(mapping)):
            if mapping[i] == "even":
                result += str(-(heappop(even)))
            if mapping[i] == "odd":
                result += str(-(heappop(odd)))
        return int("".join(result))
        
        