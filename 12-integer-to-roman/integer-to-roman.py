class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1000 : "M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        8:"VIII",
        7:"VII",
        6:"VI",
        5:"V",
        4:"IV",
        3:"III",
        2:"II",
        1:"I"}
        options = list(mapping.keys())
        concat = ""
        while num > 0 :
            for i in range(0,len(options)):
                if options[i] <= num:
                    concat += mapping[options[i]]
                    num = num - options[i]
                    break
                else:
                    pass
        return concat 