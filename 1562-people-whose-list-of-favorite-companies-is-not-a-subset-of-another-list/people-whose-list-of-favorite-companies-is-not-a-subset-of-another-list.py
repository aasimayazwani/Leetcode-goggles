class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        from collections import Counter
        mapping = []
        for i in range(0,len(favoriteCompanies)):
            person = favoriteCompanies[i]
            mapping.append(set(person))

        answer = []
        for i in range(0,len(mapping)):
            status = True
            for j in range(0,len(mapping)):
                if i!= j and mapping[i].issubset(mapping[j]):
                    status = False
                    break
                else:
                    pass
            if status == True:
                answer.append(i)
            elif status == False:
                pass
        return answer