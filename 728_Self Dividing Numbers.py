class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        correct = []
        for item in range(left,right+1):
            if self.Number(item) == True:
                correct.append(item)
        return correct 
        
    def Number(self,number):
        original_number = number
        last_digit = []
        while number:
            remaining = number % 10 
            number = int(number / 10) 
            last_digit.append(remaining)
        #print(last_digit)
        if 0 in last_digit:
            return False
        else:
            for j in range(0,len(last_digit)):
                if original_number % last_digit[j] != 0:
                    return False 
            return True