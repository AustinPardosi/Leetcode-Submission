class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        check = 0
        tempStr = str(n)

        while (check != 1) :
            temp = 0
            for i in tempStr:
                temp += (int(i)**2)
            check = temp
            tempStr = str(check)

            if (check in history) :
                return False
            else:
                history.add(check)

        return True
