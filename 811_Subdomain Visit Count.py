class Solution:
    def subdomainVisits(self, cpdomains):
        value = []
        for i in range(0,len(cpdomains)):
            value.extend(self.generate(cpdomains[i]))
        red = self.di(value)
        keys = list(red.keys())
        temp = []
        for i in range(0,len(keys)):
            temp.append(str(red[keys[i]])+" "+str(keys[i]))
        return temp
        
    def generate(self,cpdomains):
        split_value = cpdomains.split(" ")
        first = split_value[0]
        combined = split_value[1].split(".")
        last = combined[-1]
        temp= []
        for i in reversed(range(0,len(combined))):
            val = first+" "+".".join(combined[-i:])
            temp.append(val)
        return temp
    
    def di(self,value):
        temp = {}
        for i in range(0,len(value)):
            parts = value[i].split(" ")
            if parts[1] not in temp:
                temp[parts[1]] = int(parts[0])
            else:
                temp[parts[1]] += int(parts[0])
        return temp