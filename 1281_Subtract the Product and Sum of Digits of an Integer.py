class Solution:
    def subtractProductAndSum(self, n):
        l = []
        number = n 
        while number:
            remainder = number%10 
            number  = int(number/10)
            print(number)
            l.append(remainder)
        l.reverse()
        product = 1
        addition = 0 
        for i in range(0,len(l)):
            product = product*l[i]
            addition = addition + l[i]
        return product - addition