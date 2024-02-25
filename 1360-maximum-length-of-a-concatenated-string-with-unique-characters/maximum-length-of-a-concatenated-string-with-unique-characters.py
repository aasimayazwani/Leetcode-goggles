class Solution:
    def maxLength(self, arr):
        if len(arr) == 1 and len(set(arr[0])) != len(arr[0]):
            return 0
        if len(arr) == 1 and len(set(arr[0])) == len(arr[0]):
            return len(arr[0])
        
        ans = []
        def recurse(string,arr,visited):
            if len(string) != len(set(string)):
                ans.append(visited[-1])
            else:
                for i in range(0,len(arr)):
                    if arr[i] not in visited:
                        recurse(string+arr[i],arr[i:],visited + [string])
        recurse("",arr,[])
        print(ans)
        if len(ans) > 0 :
            return max([len(item) for item in ans])
        else:
            return 0 