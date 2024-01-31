class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {"I":1,
          "IV":4,
           "V":5,
          "IX":9,
          'X':10,
           "XL":40,
          "L":50,
           "XC":90,
          "C":100,
           "CD":400,
          "D":500,
           "CM":900,
           "M":1000}

        mapping = {value:key for key, value in mapping.items()}
        candidate = sorted(list(mapping.keys()),reverse=True)
        total = ""
        import math
        for i in range(0,len(candidate)):
            if candidate[i] <= num:
                print(candidate[i])
                divide = math.floor(num/candidate[i])
                total += str(mapping[candidate[i]])*divide
                num = num%candidate[i]
            else:
                pass
        return total 