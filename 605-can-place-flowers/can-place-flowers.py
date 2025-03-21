class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # array where 0,1 are present 
        # 0 -> empty 
        answer = 0 
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if (flowerbed[i-1] == 0) and (flowerbed[i] == 0) and (flowerbed[i+1] == 0) :
                flowerbed[i] = 1 
                answer +=1 
        return answer >= n