class Solution:
    def uniqueMorseRepresentations(self, words):
        e = self.morse()
        #words = ["gin", "zen", "gig", "msg"]
        total_strings = ""
        all_strings = []
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                a = e[words[i][j]]
                total_strings +=a
            all_strings.append(total_strings)
            total_strings = ""
        return len(set(all_strings))
            
    def morse(self):
        from string import ascii_lowercase
        morse = ""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = dict()
        for i in range(0,len(ascii_lowercase)):
            word = ascii_lowercase[i]
            dictionary [word] = morse[i]
        return dictionary