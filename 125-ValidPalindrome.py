class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for item in s:
            if item.isalnum():
                text += item.lower()

        if len(text) < 2:
            return True

        i, j = 0, len(text) - 1
        result = True
        while i < j:
            if text[i] != text[j]:
                return False
            i += 1
            j -= 1
        return result
