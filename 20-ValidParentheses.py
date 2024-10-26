class Solution:
    def isValid(self, s: str) -> bool:
        checkMap = {"}": "{", ")": "(", "]": "["}
        result = []

        for char in s:
            if char not in checkMap:
                result.append(char)
                continue

            if not result or checkMap[char] != result[-1]:
                return False

            result.pop(-1)

        return len(result) == 0
