class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            # Odd-length palindrome: one character is the center
            odd = self.expand(s, i, i)
            # Even-length palindrome: center is between two characters
            even = self.expand(s, i, i+1)

            # Keep the longest palindrome found so far
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result


    def expand(self, s, l, r):
        # Expand outward while characters match
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        # Pointers went one step beyond the valid palindrome, suppose start from l stop on r-1
        return s[l+1: r]