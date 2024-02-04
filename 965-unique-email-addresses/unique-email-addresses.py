class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # remove all the text after + 
        # replace the 
        # remove the last 4 letter since they will be a problematic

        emails  = [item[0:-4] for item in emails]
        answered= set()
        for i in range(0,len(emails)):
            #print(emails[i])
            details, domain = emails[i].split("@")
            details = details.replace(".","")
            if "+" in details:
                details = details.split("+")[0:-1]
                merged = details[0] + "@" + domain
            else:
                merged = details + "@" + domain
        
            answered.add(merged)
        return len(answered)