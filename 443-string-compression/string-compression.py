class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        length = len(chars)
        counting = 0
        total = ""
        for i in range(0,len(chars)):
            if chars[i] == current:
                counting +=1 
            else:
                if counting > 1:
                    total += current + str(counting)
                if counting == 1:
                    total += current
                current = chars[i]
                counting = 1 
        if total[-2:] == current + str(counting):
            chars += [item for item in total ]
            del chars[0:length]
            #print(total)
            print(chars)
            return len(chars) 
        else:
            if counting > 1:
                chars += total + current + str(counting)
            if counting ==1:
                chars += total + current
            del chars[0:length]
            return len(chars)