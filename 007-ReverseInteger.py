class Solution:
    def reverse(self, x: int) -> int:
        i = 0
        negative = False
        strRes = ""
        strX = str(x)
        while i < len(strX):
            if strX[i] == "-":
                negative = True
                i += 1
            strRes = strX[i] + strRes
            i += 1
            
        result = int(strRes)
        if negative:
            result *= -1
        
        return result

# Approach using math
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = True if x < 0 else False
        x = abs(x)

        while x:
            x, digit = divmod(x, 10)
            result = result * 10 + digit

        if not -2**31<= result <= 2**31-1:
            return 0
        
        return result if not negative else result * -1
