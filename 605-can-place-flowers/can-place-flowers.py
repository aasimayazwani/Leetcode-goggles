class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # array where 0,1 are present 
        # 0 -> empty 
        answer = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if len(list(set(flowerbed[i-1:i+2]))) == 1:
                flowerbed[i] = 1
                answer +=1 

        if answer >= n:
            return True
        return False