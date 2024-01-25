class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = ["".join(sorted(item)) for item in strs]
    
        mapping = {}
        for i in range(0,len(strs)):
            if arr[i] in mapping:
                mapping[arr[i]].append(strs[i])
            if arr[i] not in mapping:
                mapping[arr[i]] = [strs[i]]

        return list(mapping.values())