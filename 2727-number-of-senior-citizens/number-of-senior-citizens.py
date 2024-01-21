class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counting = 0 
        for i in range(0,len(details)):
            current = details[i]
            phone_number = current[0:10]
            current = current[10:]
            gender = current[0]
            current = current[1:]
            age = current[0:2]
            current = current[2:]
            if int(age) > 60:
                counting +=1 
        return counting 
