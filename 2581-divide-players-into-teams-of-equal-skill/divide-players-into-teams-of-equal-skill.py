class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        total = len(skill)/2
        target = sum(skill)/total
        ans = []
        left, right = 0, len(skill)-1
        while left < right:
            total = skill[left] + skill[right]
            if total == target:
                ans.append(skill[left]*skill[right])
                left +=1 
                right -=1 
            elif total < target:
                left +=1 
            elif total > target:
                right -=1 
        #print(ans)
        #print(total)
        if len(ans) == len(skill)/2:
            return sum(ans)
        return -1 