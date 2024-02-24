class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def recurse(word,n):
            if len(word) == n:
                ans.append(word)
            if len(word)< n:
                all_words = ["a","b","c"]
                for i in range(0,len(all_words)):
                    current = all_words[i]
                    if (len(word) > 0) and (word[-1] !=  current):
                        recurse(word+current,n)
                    if (len(word) == 0):
                        recurse(word+current,n)
        ans = []
        recurse("",n)
        ans.sort()
        if len(ans)  < k:
            return ""
        return ans[k-1]