class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {}
        mapping["2"] = [item for item in "abc"]
        mapping["3"] = [item for item in "def"]
        mapping["4"] = [item for item in "ghi"]
        mapping["5"] = [item for item in "jkl"]
        mapping["6"] = [item for item in "mno"]
        mapping["7"] = [item for item in "pqrs"]
        mapping["8"] = [item for item in "tuv"]
        mapping["9"] = [item for item in "wxyz"]
        
        def backtrack(current,string,mapping):
            if len(string) == 0:
                ans.append(current)
            else:
                test = mapping[string[0]]
                for i in range(0,len(test)):
                    backtrack(current+test[i],string[1:],mapping)
        ans = []
        backtrack("",digits,mapping)
        return ans 