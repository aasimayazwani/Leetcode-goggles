class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails = [item[:-4] for item in emails]
        valid = set()
        for i in range(0,len(emails)):
            first, second = emails[i].split("@")
            first = self.localname(first)
            current = "@".join([first,second])
            valid.add(current)
        return len(list(valid))

    def localname(self,name):
        name = name.replace(".","")
        name = name.split("+")[0]
        return name 
