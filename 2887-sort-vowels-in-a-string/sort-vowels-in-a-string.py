class Solution:
    def sortVowels(self, s: str) -> str:
        lowercase = ""
        uppercase = ""
        mapping = {"a","e","i","o","u","A","E","I","O","U"}
        for i in range(0,len(s)):
            if s[i] in mapping:
                if s[i].isupper():
                    uppercase+= s[i]
                else:
                    lowercase += s[i]
            else:
                pass 

        string = sorted(uppercase) + sorted(lowercase)
        #print(string)
        index = 0
        answer = ""
        for i in range(0,len(s)):
            if s[i] not in mapping:
                answer += s[i]
            else:
                answer += string[index]
                index +=1
        return answer 
