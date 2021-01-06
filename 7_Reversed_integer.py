class Solution(object):
    def reverse(self, x):
        
        if x < 0:
            x = abs(x)
            temp = self.Number(x)
            temp2 = self.combining(temp)
            if temp2 >= 2**31-1 or temp2 <= -2**31: 
                return 0
            else:
                return -1*temp2 
        if x ==0:
            return 0 
        if x> 0:
            temp = self.Number(x)
            temp2 = self.combining(temp)
            if temp2 >= 2**31-1 or temp2 <= -2**31: 
                return 0
            else:
                return temp2    

    def Number(self,number):
        original_number = number
        last_digit = []
        while number:
            remaining = number % 10 
            number = int(number / 10)  
            last_digit.append(remaining)
        return last_digit
    
    def combining(self,num):
        summing= 0
        i = 0
        while num:
            summing +=num[-1]*10**i
            num.pop(-1)
            i+=1
        return summing