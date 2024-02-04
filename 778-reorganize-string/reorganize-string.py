class Solution:
    def reorganizeString(self, s: str) -> str:
        # create a dictionary of the string 
        # sort the dictionary based on descending order for the dictionary
        #  if the length of the string = 0, add to the result 
        # otherwise check the newest string
        # the function is going to return the updated result string and the reduced dictionary
        # if no valid additions are possible it will return False 
        # Stopping condition is if the length of string == 0
        mapping = Counter(s)

        current_string = "0"
        while (len(mapping) > 0):
            current_string, mapping = self.get_new_word(current_string,mapping)
            if current_string == False:
                return ""
        return current_string[1:]
    

    def get_new_word(self,current_string,mapping):
        pairs = list(mapping.items())
        pairs = sorted(pairs,key = lambda x:x[1],reverse = True)
        words = [item[0] for item in pairs]
        for i in range(0,len(words)):
            if words[i] != current_string[-1]:
                current_string += words[i]
                mapping[words[i]] -=1 
                mapping = {key:value for key, value in mapping.items() if value > 0}
                return current_string, mapping
        return False, mapping
            