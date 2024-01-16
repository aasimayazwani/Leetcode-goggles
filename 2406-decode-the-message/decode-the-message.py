class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # for every new word being presented in the key assign it to the 
        # english alphabet
        # Use a hash map to keep track of the new/already assigned words. 
        # if the word had already been assigned it can't be assigned to a new word. 

        from string import ascii_lowercase
        words = list(ascii_lowercase)
        visited = {}
        key = "".join(key.split(" "))
        mapping = {}
        for i in range(0,len(key)):
            if key[i] not in visited:
                mapping[key[i]] = words[0] 
                visited[key[i]] = 1 
                words = words[1:]

            if key[i] in visited:
                pass 

        sentence = ""
        for i in range(0,len(message)):
            if message[i] != " ":
                sentence += mapping[message[i]]
            else:
                sentence += " "
        return sentence











