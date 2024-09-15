class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s):
            left, right = 0 , len(s)-1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left +=1 
                right -=1 
            return True


        def checking(arr):
            for i in range(0,len(arr)):
                if len(arr[i]) ==1:
                    pass 
                if len(arr[i]) > 1:
                    #print(arr[i])
                    if check(arr[i]) == False:
                        return False
            return True

        ans = []        
        def total(current, s):
            if len(s) ==0:
                ans.append(current.split("."))
            else:
                if len(current) > 0:
                    total(current + "." + s[0], s[1:])
                total(current + s[0], s[1:])
        total("",s)

        answer = []
        for i in range(0,len(ans)):
            if checking(ans[i]):
                answer.append(ans[i])
        return answer 
        